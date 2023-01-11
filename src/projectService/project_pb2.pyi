from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProjectRequest(_message.Message):
    __slots__ = ["name", "user_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateTagRequest(_message.Message):
    __slots__ = ["name", "project_id", "user_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ["project_id", "user_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class ProjectResponse(_message.Message):
    __slots__ = ["id", "name", "tags"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    tags: _containers.RepeatedCompositeFieldContainer[TagResponse]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[TagResponse, _Mapping]]] = ...) -> None: ...

class TagResponse(_message.Message):
    __slots__ = ["id", "name", "project_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    project_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...
