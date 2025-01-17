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

from proto.print_pb2 import PrintDocument, PrintJob, JobStatus, PrintSettings

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

    ETA_SIZE = {
        PrintSettings.PAPER_SIZE_A5: 0.5,
        PrintSettings.PAPER_SIZE_A4: 1,
        PrintSettings.PAPER_SIZE_A3: 2,
        PrintSettings.PAPER_SIZE_A2: 4,
    }

    def SubmitPrintJob(self, request: PrintDocument, context: grpc.ServicerContext):
        copies = request.settings.copies
        if job_queue.full() or len(job_queue.queue) + copies > job_queue.maxsize:
            context.abort(grpc.StatusCode.RESOURCE_EXHAUSTED, "Job queue is full")
        req_file = PyPDF2.PdfReader(stream=BytesIO(request.content))
        print_jobs = []
        for _ in range(copies):
            print_job = PrintJob(
                job_id=str(uuid.uuid4()),
                document_id=request.document_id,
                total_pages=len(req_file.pages),
                pages_printed=0,
                status=JobStatus.JOB_STATUS_PENDING,
                eta_seconds=self._calc_eta(
                    len(req_file.pages), request.settings.paper_size
                ),
            )
            documents[request.document_id] = request
            jobs[print_job.job_id] = print_job
            job_queue.put(print_job)
            print_jobs.append(print_job)
        return ListPrintJobsResponse(jobs=print_jobs)

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
        return ListPrintJobsResponse(jobs=list(job_queue.queue) + [running_job])

    def ViewPrinterStatus(self, request, context):
        global printer_status
        return PrinterStatus(status=printer_status, job=running_job)

    @staticmethod
    def _calc_eta(pages: int, size: PrintSettings.PaperSize, pages_printed: int = 0):
        return VirtualPrinterService.ETA_SIZE[size] * (pages - pages_printed)


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
        document = documents[job.document_id]
        size = document.settings.paper_size
        for i in range(job.total_pages):
            job.pages_printed = i + 1
            if job.status == JobStatus.JOB_STATUS_CANCELLED:
                break
            job.eta_seconds = VirtualPrinterService._calc_eta(
                job.total_pages, size, job.pages_printed
            )
            time.sleep(VirtualPrinterService.ETA_SIZE[size])
        job.status = JobStatus.JOB_STATUS_COMPLETED
        job_queue.task_done()
        running_job = None
        printer_status = PrinterStatus.STATUS_IDLE
        time.sleep(1)
        if job_queue.empty():
            documents = {}


def serve(PORT: int):
    interceptors = [ExceptionToStatusInterceptor()]
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
    l = threading.Thread(target=serve, args=(sys.argv[1],))
    w = threading.Thread(target=worker)
    l.start()
    w.start()
    l.join()
    w.join()
