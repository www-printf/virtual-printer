# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/print_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'proto/print_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import print_pb2 as proto_dot_print__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto/print_service.proto\x12\x07printer\x1a\x11proto/print.proto\"%\n\x13GetJobStatusRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\"\n\x10\x43\x61ncelJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"8\n\x15ListPrintJobsResponse\x12\x1f\n\x04jobs\x18\x01 \x03(\x0b\x32\x11.printer.PrintJob\"\xb8\x01\n\rPrinterStatus\x12-\n\x06status\x18\x01 \x01(\x0e\x32\x1d.printer.PrinterStatus.Status\x12\x1e\n\x03job\x18\x02 \x01(\x0b\x32\x11.printer.PrintJob\"X\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSTATUS_IDLE\x10\x01\x12\x13\n\x0fSTATUS_PRINTING\x10\x02\x12\x10\n\x0cSTATUS_ERROR\x10\x03\"\x07\n\x05\x45mpty2\xab\x03\n\x0eVirtualPrinter\x12J\n\x0eSubmitPrintJob\x12\x16.printer.PrintDocument\x1a\x1e.printer.ListPrintJobsResponse\"\x00\x12\x41\n\x0cGetJobStatus\x12\x1c.printer.GetJobStatusRequest\x1a\x11.printer.PrintJob\"\x00\x12@\n\x0e\x43\x61ncelPrintJob\x12\x19.printer.CancelJobRequest\x1a\x11.printer.PrintJob\"\x00\x12\x46\n\x0fMonitorPrintJob\x12\x1c.printer.GetJobStatusRequest\x1a\x11.printer.PrintJob\"\x00\x30\x01\x12\x41\n\rListPrintJobs\x12\x0e.printer.Empty\x1a\x1e.printer.ListPrintJobsResponse\"\x00\x12=\n\x11ViewPrinterStatus\x12\x0e.printer.Empty\x1a\x16.printer.PrinterStatus\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.print_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETJOBSTATUSREQUEST']._serialized_start=57
  _globals['_GETJOBSTATUSREQUEST']._serialized_end=94
  _globals['_CANCELJOBREQUEST']._serialized_start=96
  _globals['_CANCELJOBREQUEST']._serialized_end=130
  _globals['_LISTPRINTJOBSRESPONSE']._serialized_start=132
  _globals['_LISTPRINTJOBSRESPONSE']._serialized_end=188
  _globals['_PRINTERSTATUS']._serialized_start=191
  _globals['_PRINTERSTATUS']._serialized_end=375
  _globals['_PRINTERSTATUS_STATUS']._serialized_start=287
  _globals['_PRINTERSTATUS_STATUS']._serialized_end=375
  _globals['_EMPTY']._serialized_start=377
  _globals['_EMPTY']._serialized_end=384
  _globals['_VIRTUALPRINTER']._serialized_start=387
  _globals['_VIRTUALPRINTER']._serialized_end=814
# @@protoc_insertion_point(module_scope)
