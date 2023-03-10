# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x05users\"`\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x11\n\tjwt_token\x18\x04 \x01(\t\x12\x12\n\nexpiration\x18\x05 \x01(\t\".\n\x08LoginReq\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"R\n\x08LoginRsp\x12\x11\n\tjwt_token\x18\x01 \x01(\t\x12\x12\n\nexpiration\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0f\n\x07message\x18\x04 \x01(\t\"@\n\x0bRegisterReq\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\".\n\x0bRegisterRsp\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"A\n\x0bValidateReq\x12\x11\n\tjwt_token\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"U\n\x0bValidateRsp\x12\x11\n\tjwt_token\x18\x01 \x01(\t\x12\x12\n\nexpiration\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0f\n\x07message\x18\x04 \x01(\t2\xa0\x01\n\x05Users\x12+\n\x05Login\x12\x0f.users.LoginReq\x1a\x0f.users.LoginRsp\"\x00\x12\x34\n\x08Register\x12\x12.users.RegisterReq\x1a\x12.users.RegisterRsp\"\x00\x12\x34\n\x08Validate\x12\x12.users.ValidateReq\x1a\x12.users.ValidateRsp\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=21
  _USER._serialized_end=117
  _LOGINREQ._serialized_start=119
  _LOGINREQ._serialized_end=165
  _LOGINRSP._serialized_start=167
  _LOGINRSP._serialized_end=249
  _REGISTERREQ._serialized_start=251
  _REGISTERREQ._serialized_end=315
  _REGISTERRSP._serialized_start=317
  _REGISTERRSP._serialized_end=363
  _VALIDATEREQ._serialized_start=365
  _VALIDATEREQ._serialized_end=430
  _VALIDATERSP._serialized_start=432
  _VALIDATERSP._serialized_end=517
  _USERS._serialized_start=520
  _USERS._serialized_end=680
# @@protoc_insertion_point(module_scope)
