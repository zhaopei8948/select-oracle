# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: select.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='select.proto',
  package='select',
  syntax='proto3',
  serialized_options=_b('\n\027io.grpc.examples.selectB\013SelectProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x0cselect.proto\x12\x06select\"\x1c\n\rSelectRequest\x12\x0b\n\x03sql\x18\x01 \x01(\t\"T\n\x0bSelectReply\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.select.SelectReply.Result\x1a\x18\n\x06Result\x12\x0e\n\x06\x66ields\x18\x01 \x03(\t2I\n\x07Greeter\x12>\n\x0eSelectDatabase\x12\x15.select.SelectRequest\x1a\x13.select.SelectReply\"\x00\x42.\n\x17io.grpc.examples.selectB\x0bSelectProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_SELECTREQUEST = _descriptor.Descriptor(
  name='SelectRequest',
  full_name='select.SelectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sql', full_name='select.SelectRequest.sql', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=52,
)


_SELECTREPLY_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='select.SelectReply.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='select.SelectReply.Result.fields', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=138,
)

_SELECTREPLY = _descriptor.Descriptor(
  name='SelectReply',
  full_name='select.SelectReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='select.SelectReply.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SELECTREPLY_RESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=138,
)

_SELECTREPLY_RESULT.containing_type = _SELECTREPLY
_SELECTREPLY.fields_by_name['results'].message_type = _SELECTREPLY_RESULT
DESCRIPTOR.message_types_by_name['SelectRequest'] = _SELECTREQUEST
DESCRIPTOR.message_types_by_name['SelectReply'] = _SELECTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SelectRequest = _reflection.GeneratedProtocolMessageType('SelectRequest', (_message.Message,), dict(
  DESCRIPTOR = _SELECTREQUEST,
  __module__ = 'select_pb2'
  # @@protoc_insertion_point(class_scope:select.SelectRequest)
  ))
_sym_db.RegisterMessage(SelectRequest)

SelectReply = _reflection.GeneratedProtocolMessageType('SelectReply', (_message.Message,), dict(

  Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
    DESCRIPTOR = _SELECTREPLY_RESULT,
    __module__ = 'select_pb2'
    # @@protoc_insertion_point(class_scope:select.SelectReply.Result)
    ))
  ,
  DESCRIPTOR = _SELECTREPLY,
  __module__ = 'select_pb2'
  # @@protoc_insertion_point(class_scope:select.SelectReply)
  ))
_sym_db.RegisterMessage(SelectReply)
_sym_db.RegisterMessage(SelectReply.Result)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='select.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=140,
  serialized_end=213,
  methods=[
  _descriptor.MethodDescriptor(
    name='SelectDatabase',
    full_name='select.Greeter.SelectDatabase',
    index=0,
    containing_service=None,
    input_type=_SELECTREQUEST,
    output_type=_SELECTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
