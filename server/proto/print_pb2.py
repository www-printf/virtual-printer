# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/print.proto
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
    'proto/print.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/print.proto\x12\x07printer\x1a\x1fgoogle/protobuf/timestamp.proto\"m\n\rPrintDocument\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12(\n\x08settings\x18\x04 \x01(\x0b\x32\x16.printer.PrintSettings\"\x94\x04\n\rPrintSettings\x12\x34\n\ncolor_mode\x18\x01 \x01(\x0e\x32 .printer.PrintSettings.ColorMode\x12\x34\n\npaper_size\x18\x02 \x01(\x0e\x32 .printer.PrintSettings.PaperSize\x12\x37\n\x0borientation\x18\x03 \x01(\x0e\x32\".printer.PrintSettings.Orientation\x12\x0e\n\x06\x63opies\x18\x04 \x01(\x05\x12\x14\n\x0c\x64ouble_sided\x18\x05 \x01(\x08\"]\n\tColorMode\x12 \n\x1c\x43OLOR_MODE_COLOR_UNSPECIFIED\x10\x00\x12\x14\n\x10\x43OLOR_MODE_COLOR\x10\x01\x12\x18\n\x14\x43OLOR_MODE_GRAYSCALE\x10\x02\"x\n\tPaperSize\x12\x1f\n\x1bPAPER_SIZE_SIZE_UNSPECIFIED\x10\x00\x12\x11\n\rPAPER_SIZE_A5\x10\x01\x12\x11\n\rPAPER_SIZE_A4\x10\x02\x12\x11\n\rPAPER_SIZE_A3\x10\x03\x12\x11\n\rPAPER_SIZE_A2\x10\x04\"_\n\x0bOrientation\x12\x1b\n\x17ORIENTATION_UNSPECIFIED\x10\x00\x12\x18\n\x14ORIENTATION_PORTRAIT\x10\x01\x12\x19\n\x15ORIENTATION_LANDSCAPE\x10\x02\"\xc6\x01\n\x08PrintJob\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64ocument_id\x18\x02 \x01(\t\x12\x30\n\x0csubmitted_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x06status\x18\x04 \x01(\x0e\x32\x12.printer.JobStatus\x12\x15\n\rpages_printed\x18\x05 \x01(\x05\x12\x13\n\x0btotal_pages\x18\x06 \x01(\x05\x12\x13\n\x0b\x65ta_seconds\x18\x07 \x01(\x05*\xa5\x01\n\tJobStatus\x12\x1a\n\x16JOB_STATUS_UNSPECIFIED\x10\x00\x12\x16\n\x12JOB_STATUS_PENDING\x10\x01\x12\x19\n\x15JOB_STATUS_PROCESSING\x10\x02\x12\x18\n\x14JOB_STATUS_COMPLETED\x10\x03\x12\x15\n\x11JOB_STATUS_FAILED\x10\x04\x12\x18\n\x14JOB_STATUS_CANCELLED\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.print_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOBSTATUS']._serialized_start=911
  _globals['_JOBSTATUS']._serialized_end=1076
  _globals['_PRINTDOCUMENT']._serialized_start=63
  _globals['_PRINTDOCUMENT']._serialized_end=172
  _globals['_PRINTSETTINGS']._serialized_start=175
  _globals['_PRINTSETTINGS']._serialized_end=707
  _globals['_PRINTSETTINGS_COLORMODE']._serialized_start=395
  _globals['_PRINTSETTINGS_COLORMODE']._serialized_end=488
  _globals['_PRINTSETTINGS_PAPERSIZE']._serialized_start=490
  _globals['_PRINTSETTINGS_PAPERSIZE']._serialized_end=610
  _globals['_PRINTSETTINGS_ORIENTATION']._serialized_start=612
  _globals['_PRINTSETTINGS_ORIENTATION']._serialized_end=707
  _globals['_PRINTJOB']._serialized_start=710
  _globals['_PRINTJOB']._serialized_end=908
# @@protoc_insertion_point(module_scope)
