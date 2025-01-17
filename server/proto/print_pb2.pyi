from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATUS_UNSPECIFIED: _ClassVar[JobStatus]
    JOB_STATUS_PENDING: _ClassVar[JobStatus]
    JOB_STATUS_PROCESSING: _ClassVar[JobStatus]
    JOB_STATUS_COMPLETED: _ClassVar[JobStatus]
    JOB_STATUS_FAILED: _ClassVar[JobStatus]
    JOB_STATUS_CANCELLED: _ClassVar[JobStatus]
JOB_STATUS_UNSPECIFIED: JobStatus
JOB_STATUS_PENDING: JobStatus
JOB_STATUS_PROCESSING: JobStatus
JOB_STATUS_COMPLETED: JobStatus
JOB_STATUS_FAILED: JobStatus
JOB_STATUS_CANCELLED: JobStatus

class PrintDocument(_message.Message):
    __slots__ = ("document_id", "name", "content", "settings")
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    document_id: str
    name: str
    content: bytes
    settings: PrintSettings
    def __init__(self, document_id: _Optional[str] = ..., name: _Optional[str] = ..., content: _Optional[bytes] = ..., settings: _Optional[_Union[PrintSettings, _Mapping]] = ...) -> None: ...

class PrintSettings(_message.Message):
    __slots__ = ("color_mode", "paper_size", "orientation", "copies", "double_sided")
    class ColorMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_MODE_COLOR_UNSPECIFIED: _ClassVar[PrintSettings.ColorMode]
        COLOR_MODE_COLOR: _ClassVar[PrintSettings.ColorMode]
        COLOR_MODE_GRAYSCALE: _ClassVar[PrintSettings.ColorMode]
    COLOR_MODE_COLOR_UNSPECIFIED: PrintSettings.ColorMode
    COLOR_MODE_COLOR: PrintSettings.ColorMode
    COLOR_MODE_GRAYSCALE: PrintSettings.ColorMode
    class PaperSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAPER_SIZE_SIZE_UNSPECIFIED: _ClassVar[PrintSettings.PaperSize]
        PAPER_SIZE_A5: _ClassVar[PrintSettings.PaperSize]
        PAPER_SIZE_A4: _ClassVar[PrintSettings.PaperSize]
        PAPER_SIZE_A3: _ClassVar[PrintSettings.PaperSize]
        PAPER_SIZE_A2: _ClassVar[PrintSettings.PaperSize]
    PAPER_SIZE_SIZE_UNSPECIFIED: PrintSettings.PaperSize
    PAPER_SIZE_A5: PrintSettings.PaperSize
    PAPER_SIZE_A4: PrintSettings.PaperSize
    PAPER_SIZE_A3: PrintSettings.PaperSize
    PAPER_SIZE_A2: PrintSettings.PaperSize
    class Orientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORIENTATION_UNSPECIFIED: _ClassVar[PrintSettings.Orientation]
        ORIENTATION_PORTRAIT: _ClassVar[PrintSettings.Orientation]
        ORIENTATION_LANDSCAPE: _ClassVar[PrintSettings.Orientation]
    ORIENTATION_UNSPECIFIED: PrintSettings.Orientation
    ORIENTATION_PORTRAIT: PrintSettings.Orientation
    ORIENTATION_LANDSCAPE: PrintSettings.Orientation
    COLOR_MODE_FIELD_NUMBER: _ClassVar[int]
    PAPER_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    COPIES_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_SIDED_FIELD_NUMBER: _ClassVar[int]
    color_mode: PrintSettings.ColorMode
    paper_size: PrintSettings.PaperSize
    orientation: PrintSettings.Orientation
    copies: int
    double_sided: bool
    def __init__(self, color_mode: _Optional[_Union[PrintSettings.ColorMode, str]] = ..., paper_size: _Optional[_Union[PrintSettings.PaperSize, str]] = ..., orientation: _Optional[_Union[PrintSettings.Orientation, str]] = ..., copies: _Optional[int] = ..., double_sided: bool = ...) -> None: ...

class PrintJob(_message.Message):
    __slots__ = ("job_id", "document_id", "submitted_at", "status", "pages_printed", "total_pages", "eta_seconds")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGES_PRINTED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    ETA_SECONDS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    document_id: str
    submitted_at: _timestamp_pb2.Timestamp
    status: JobStatus
    pages_printed: int
    total_pages: int
    eta_seconds: int
    def __init__(self, job_id: _Optional[str] = ..., document_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[JobStatus, str]] = ..., pages_printed: _Optional[int] = ..., total_pages: _Optional[int] = ..., eta_seconds: _Optional[int] = ...) -> None: ...
