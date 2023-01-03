from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Audit(_message.Message):
    __slots__ = ["created_at", "created_by", "data", "deleted_at", "deleted_by", "description", "id", "name", "status", "type", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: str
    created_by: str
    data: str
    deleted_at: str
    deleted_by: str
    description: str
    id: str
    name: str
    status: str
    type: str
    updated_at: str
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., data: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_at: _Optional[str] = ..., updated_by: _Optional[str] = ..., deleted_at: _Optional[str] = ..., deleted_by: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CreateAuditRequest(_message.Message):
    __slots__ = ["created_at", "created_by", "data", "deleted_at", "deleted_by", "description", "name", "status", "type", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: str
    created_by: str
    data: str
    deleted_at: str
    deleted_by: str
    description: str
    name: str
    status: str
    type: str
    updated_at: str
    updated_by: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., data: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_at: _Optional[str] = ..., updated_by: _Optional[str] = ..., deleted_at: _Optional[str] = ..., deleted_by: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CreateAuditResponse(_message.Message):
    __slots__ = ["audit", "message", "status"]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    audit: Audit
    message: str
    status: int
    def __init__(self, audit: _Optional[_Union[Audit, _Mapping]] = ..., status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class DeleteAuditRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteAuditResponse(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: int
    def __init__(self, status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class GetAuditRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAuditResponse(_message.Message):
    __slots__ = ["audit", "message", "status"]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    audit: Audit
    message: str
    status: int
    def __init__(self, audit: _Optional[_Union[Audit, _Mapping]] = ..., status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class GetAuditsRequest(_message.Message):
    __slots__ = ["created_at", "created_by", "data", "deleted_at", "deleted_by", "description", "id", "name", "status", "type", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: str
    created_by: str
    data: str
    deleted_at: str
    deleted_by: str
    description: str
    id: str
    name: str
    status: str
    type: str
    updated_at: str
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., data: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_at: _Optional[str] = ..., updated_by: _Optional[str] = ..., deleted_at: _Optional[str] = ..., deleted_by: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class GetAuditsResponse(_message.Message):
    __slots__ = ["audits", "message", "status"]
    AUDITS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    audits: _containers.RepeatedCompositeFieldContainer[Audit]
    message: str
    status: int
    def __init__(self, audits: _Optional[_Iterable[_Union[Audit, _Mapping]]] = ..., status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateAuditRequest(_message.Message):
    __slots__ = ["created_at", "created_by", "data", "deleted_at", "deleted_by", "description", "id", "name", "status", "type", "updated_at", "updated_by"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    created_at: str
    created_by: str
    data: str
    deleted_at: str
    deleted_by: str
    description: str
    id: str
    name: str
    status: str
    type: str
    updated_at: str
    updated_by: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., data: _Optional[str] = ..., status: _Optional[str] = ..., created_at: _Optional[str] = ..., created_by: _Optional[str] = ..., updated_at: _Optional[str] = ..., updated_by: _Optional[str] = ..., deleted_at: _Optional[str] = ..., deleted_by: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class UpdateAuditResponse(_message.Message):
    __slots__ = ["audit", "message", "status"]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    audit: Audit
    message: str
    status: int
    def __init__(self, audit: _Optional[_Union[Audit, _Mapping]] = ..., status: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
