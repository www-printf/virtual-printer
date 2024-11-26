from proto import print_pb2 as _print_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetJobStatusRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class ListPrintJobsResponse(_message.Message):
    __slots__ = ("jobs",)
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[_print_pb2.PrintJob]
    def __init__(self, jobs: _Optional[_Iterable[_Union[_print_pb2.PrintJob, _Mapping]]] = ...) -> None: ...

class PrinterStatus(_message.Message):
    __slots__ = ("status", "job")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[PrinterStatus.Status]
        STATUS_IDLE: _ClassVar[PrinterStatus.Status]
        STATUS_PRINTING: _ClassVar[PrinterStatus.Status]
        STATUS_ERROR: _ClassVar[PrinterStatus.Status]
    STATUS_UNSPECIFIED: PrinterStatus.Status
    STATUS_IDLE: PrinterStatus.Status
    STATUS_PRINTING: PrinterStatus.Status
    STATUS_ERROR: PrinterStatus.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    status: PrinterStatus.Status
    job: _print_pb2.PrintJob
    def __init__(self, status: _Optional[_Union[PrinterStatus.Status, str]] = ..., job: _Optional[_Union[_print_pb2.PrintJob, _Mapping]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
