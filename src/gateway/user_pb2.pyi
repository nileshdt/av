from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginReq(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginRsp(_message.Message):
    __slots__ = ["expiration", "jwt_token"]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    JWT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    expiration: str
    jwt_token: str
    def __init__(self, jwt_token: _Optional[str] = ..., expiration: _Optional[str] = ...) -> None: ...

class RegisterReq(_message.Message):
    __slots__ = ["email", "password", "username"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class RegisterRsp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
