# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ROSEnums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eROSEnums.proto*!\n\x04Type\x12\x0b\n\x07REQUEST\x10\x00\x12\x0c\n\x08RESPONSE\x10\x01*_\n\x06Method\x12\x0b\n\x07OPTIONS\x10\x00\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04HEAD\x10\x02\x12\x08\n\x04POST\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\t\n\x05TRACE\x10\x06\x12\x0b\n\x07\x43ONNECT\x10\x07')

_TYPE = DESCRIPTOR.enum_types_by_name['Type']
Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
_METHOD = DESCRIPTOR.enum_types_by_name['Method']
Method = enum_type_wrapper.EnumTypeWrapper(_METHOD)
REQUEST = 0
RESPONSE = 1
OPTIONS = 0
GET = 1
HEAD = 2
POST = 3
PUT = 4
DELETE = 5
TRACE = 6
CONNECT = 7


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TYPE._serialized_start=18
  _TYPE._serialized_end=51
  _METHOD._serialized_start=53
  _METHOD._serialized_end=148
# @@protoc_insertion_point(module_scope)