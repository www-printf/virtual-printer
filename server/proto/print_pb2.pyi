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
        PAPER_SIZE_A6: _ClassVar[PrintSettings.PaperSize]
    PAPER_SIZE_SIZE_UNSPECIFIED: PrintSettings.PaperSize
    PAPER_SIZE_A5: PrintSettings.PaperSize
    PAPER_SIZE_A4: PrintSettings.PaperSize
    PAPER_SIZE_A3: PrintSettings.PaperSize
    PAPER_SIZE_A6: PrintSettings.PaperSize
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
    __slots__ = ("job_id", "document_id", "submitted_at", "status", "pages_printed", "total_pages")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGES_PRINTED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGES_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    document_id: str
    submitted_at: _timestamp_pb2.Timestamp
    status: JobStatus
    pages_printed: int
    total_pages: int
    def __init__(self, job_id: _Optional[str] = ..., document_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[JobStatus, str]] = ..., pages_printed: _Optional[int] = ..., total_pages: _Optional[int] = ...) -> None: ...

class PrinterStatus(_message.Message):
    __slots__ = ("state", "error_message", "jobs_in_queue", "paper_jam", "paper_level", "toner_level")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PrinterStatus.State]
        STATE_READY: _ClassVar[PrinterStatus.State]
        STATE_BUSY: _ClassVar[PrinterStatus.State]
        STATE_ERROR: _ClassVar[PrinterStatus.State]
        STATE_OFFLINE: _ClassVar[PrinterStatus.State]
    STATE_UNSPECIFIED: PrinterStatus.State
    STATE_READY: PrinterStatus.State
    STATE_BUSY: PrinterStatus.State
    STATE_ERROR: PrinterStatus.State
    STATE_OFFLINE: PrinterStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    JOBS_IN_QUEUE_FIELD_NUMBER: _ClassVar[int]
    PAPER_JAM_FIELD_NUMBER: _ClassVar[int]
    PAPER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TONER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    state: PrinterStatus.State
    error_message: str
    jobs_in_queue: int
    paper_jam: bool
    paper_level: int
    toner_level: int
    def __init__(self, state: _Optional[_Union[PrinterStatus.State, str]] = ..., error_message: _Optional[str] = ..., jobs_in_queue: _Optional[int] = ..., paper_jam: bool = ..., paper_level: _Optional[int] = ..., toner_level: _Optional[int] = ...) -> None: ...
