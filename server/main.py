#!/usr/bin/env python3
import logging

from concurrent import futures
import threading

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from proto.print_service_pb2_grpc import (
    add_VirtualPrinterServicer_to_server,
    VirtualPrinterServicer,
)

from proto.print_service_pb2 import (
    GetJobStatusRequest,
    CancelJobRequest,
    ListPrintJobsResponse,
    PrinterStatus,
)

from proto.print_pb2 import PrintDocument, PrintJob, JobStatus

import PyPDF2
from io import BytesIO
import uuid
import queue
import time

job_queue = queue.Queue(maxsize=10)
jobs = {}
documents = {}
running_job = None

printer_status = PrinterStatus.STATUS_IDLE


class VirtualPrinterService(VirtualPrinterServicer):

    def SubmitPrintJob(self, request: PrintDocument, context: grpc.ServicerContext):
        if job_queue.full():
            context.abort(grpc.StatusCode.RESOURCE_EXHAUSTED, "Job queue is full")
        req_file = PyPDF2.PdfReader(stream=BytesIO(request.content))
        print_job = PrintJob(
            job_id=str(uuid.uuid4()),
            document_id=request.document_id,
            total_pages=len(req_file.pages),
            pages_printed=0,
            status=JobStatus.JOB_STATUS_PENDING,
        )
        documents[request.document_id] = request
        jobs[print_job.job_id] = print_job
        job_queue.put(print_job)
        return print_job

    def GetJobStatus(self, request: GetJobStatusRequest, context: grpc.ServicerContext):
        if request.job_id in jobs:
            return jobs[request.job_id]
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Job not found")

    def CancelPrintJob(self, request: CancelJobRequest, context):
        if request.job_id in jobs:
            job = jobs[request.job_id]
            if job.status == JobStatus.JOB_STATUS_PENDING:
                job.status = JobStatus.JOB_STATUS_CANCELED
                return job
            else:
                context.abort(grpc.StatusCode.FAILED_PRECONDITION, "Job not cancelable")
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, "Job not found")

    def MonitorPrintJob(self, request: GetJobStatusRequest, context):
        job = jobs.get(request.job_id)
        if job is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Job not found")
        while True:
            yield job

    def ListPrintJobs(self, request, context):
        return ListPrintJobsResponse(jobs=list(job_queue.queue))

    def ViewPrinterStatus(self, request, context):
        global printer_status
        return PrinterStatus(status=printer_status, job=running_job)


class AuthInterceptor(grpc.ServerInterceptor):
    def __init__(self, token):
        self.token = token

    def intercept_service(self, continuation, handler_call_details):
        if (
            self.token
            and handler_call_details.metadata.get("authorization") != self.token
        ):
            raise grpc.RpcError(
                grpc.StatusCode.UNAUTHENTICATED, "Invalid token provided"
            )
        return continuation(handler_call_details)


def worker():
    global printer_status
    global job_queue
    global running_job
    while True:
        job = job_queue.get()
        job.status = JobStatus.JOB_STATUS_PROCESSING
        printer_status = PrinterStatus.STATUS_PRINTING
        running_job = job
        for i in range(job.total_pages):
            job.pages_printed = i + 1
            if job.status == JobStatus.JOB_STATUS_CANCELLED:
                break
            time.sleep(1)
        job.status = JobStatus.JOB_STATUS_COMPLETED
        job_queue.task_done()
        running_job = None
        printer_status = PrinterStatus.STATUS_IDLE
        documents.pop(job.document_id)
        time.sleep(1)


def serve(PORT: int, key: str = None):
    interceptors = [ExceptionToStatusInterceptor(), AuthInterceptor(key)]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_VirtualPrinterServicer_to_server(VirtualPrinterService(), server)
    server.add_insecure_port("[::]:{}".format(PORT))
    logging.info("Starting server on port %s", PORT)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    import sys
    import os

    logging.basicConfig(level=os.getenv("LOGLEVEL", "INFO"))
    if len(sys.argv) != 2:
        print("Usage: {} PORT".format(sys.argv[0]))
        sys.exit(1)
    l = threading.Thread(
        target=serve, args=(sys.argv[1], os.getenv("AUTH_TOKEN", None))
    )
    w = threading.Thread(target=worker)
    l.start()
    w.start()
    l.join()
    w.join()
