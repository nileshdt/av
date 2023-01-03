from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendReq(_message.Message):
    __slots__ = ["body", "email", "subject", "to"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    body: str
    email: str
    subject: str
    to: str
    def __init__(self, email: _Optional[str] = ..., to: _Optional[str] = ..., subject: _Optional[str] = ..., body: _Optional[str] = ...) -> None: ...

class SendRes(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: int
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
