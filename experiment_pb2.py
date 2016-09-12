# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='experiment.proto',
  package='experiment',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x65xperiment.proto\x12\nexperiment\"&\n\nExperiment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1a\n\x0c\x45xperimentId\x12\n\n\x02id\x18\x01 \x01(\t\"\"\n\x10\x45xperimentStatus\x12\x0e\n\x06status\x18\x01 \x01(\t2\xf9\x01\n\x11\x45xperimentService\x12I\n\x0fStartExperiment\x12\x16.experiment.Experiment\x1a\x1c.experiment.ExperimentStatus\"\x00\x12H\n\x0eStopExperiment\x12\x16.experiment.Experiment\x1a\x1c.experiment.ExperimentStatus\"\x00\x12O\n\x13GetExperimentStatus\x12\x18.experiment.ExperimentId\x1a\x1c.experiment.ExperimentStatus\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='experiment.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='experiment.Experiment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='experiment.Experiment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=70,
)


_EXPERIMENTID = _descriptor.Descriptor(
  name='ExperimentId',
  full_name='experiment.ExperimentId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='experiment.ExperimentId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=98,
)


_EXPERIMENTSTATUS = _descriptor.Descriptor(
  name='ExperimentStatus',
  full_name='experiment.ExperimentStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='experiment.ExperimentStatus.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['ExperimentId'] = _EXPERIMENTID
DESCRIPTOR.message_types_by_name['ExperimentStatus'] = _EXPERIMENTSTATUS

Experiment = _reflection.GeneratedProtocolMessageType('Experiment', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENT,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:experiment.Experiment)
  ))
_sym_db.RegisterMessage(Experiment)

ExperimentId = _reflection.GeneratedProtocolMessageType('ExperimentId', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTID,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:experiment.ExperimentId)
  ))
_sym_db.RegisterMessage(ExperimentId)

ExperimentStatus = _reflection.GeneratedProtocolMessageType('ExperimentStatus', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTSTATUS,
  __module__ = 'experiment_pb2'
  # @@protoc_insertion_point(class_scope:experiment.ExperimentStatus)
  ))
_sym_db.RegisterMessage(ExperimentStatus)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ExperimentServiceStub(object):
  """The Experiment service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartExperiment = channel.unary_unary(
        '/experiment.ExperimentService/StartExperiment',
        request_serializer=Experiment.SerializeToString,
        response_deserializer=ExperimentStatus.FromString,
        )
    self.StopExperiment = channel.unary_unary(
        '/experiment.ExperimentService/StopExperiment',
        request_serializer=Experiment.SerializeToString,
        response_deserializer=ExperimentStatus.FromString,
        )
    self.GetExperimentStatus = channel.unary_unary(
        '/experiment.ExperimentService/GetExperimentStatus',
        request_serializer=ExperimentId.SerializeToString,
        response_deserializer=ExperimentStatus.FromString,
        )


class ExperimentServiceServicer(object):
  """The Experiment service definition.
  """

  def StartExperiment(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopExperiment(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExperimentStatus(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExperimentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.StartExperiment,
          request_deserializer=Experiment.FromString,
          response_serializer=ExperimentStatus.SerializeToString,
      ),
      'StopExperiment': grpc.unary_unary_rpc_method_handler(
          servicer.StopExperiment,
          request_deserializer=Experiment.FromString,
          response_serializer=ExperimentStatus.SerializeToString,
      ),
      'GetExperimentStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetExperimentStatus,
          request_deserializer=ExperimentId.FromString,
          response_serializer=ExperimentStatus.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'experiment.ExperimentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaExperimentServiceServicer(object):
  """The Experiment service definition.
  """
  def StartExperiment(self, request, context):
    """Sends a greeting
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def StopExperiment(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetExperimentStatus(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaExperimentServiceStub(object):
  """The Experiment service definition.
  """
  def StartExperiment(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends a greeting
    """
    raise NotImplementedError()
  StartExperiment.future = None
  def StopExperiment(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  StopExperiment.future = None
  def GetExperimentStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  GetExperimentStatus.future = None


def beta_create_ExperimentService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('experiment.ExperimentService', 'GetExperimentStatus'): ExperimentId.FromString,
    ('experiment.ExperimentService', 'StartExperiment'): Experiment.FromString,
    ('experiment.ExperimentService', 'StopExperiment'): Experiment.FromString,
  }
  response_serializers = {
    ('experiment.ExperimentService', 'GetExperimentStatus'): ExperimentStatus.SerializeToString,
    ('experiment.ExperimentService', 'StartExperiment'): ExperimentStatus.SerializeToString,
    ('experiment.ExperimentService', 'StopExperiment'): ExperimentStatus.SerializeToString,
  }
  method_implementations = {
    ('experiment.ExperimentService', 'GetExperimentStatus'): face_utilities.unary_unary_inline(servicer.GetExperimentStatus),
    ('experiment.ExperimentService', 'StartExperiment'): face_utilities.unary_unary_inline(servicer.StartExperiment),
    ('experiment.ExperimentService', 'StopExperiment'): face_utilities.unary_unary_inline(servicer.StopExperiment),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ExperimentService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('experiment.ExperimentService', 'GetExperimentStatus'): ExperimentId.SerializeToString,
    ('experiment.ExperimentService', 'StartExperiment'): Experiment.SerializeToString,
    ('experiment.ExperimentService', 'StopExperiment'): Experiment.SerializeToString,
  }
  response_deserializers = {
    ('experiment.ExperimentService', 'GetExperimentStatus'): ExperimentStatus.FromString,
    ('experiment.ExperimentService', 'StartExperiment'): ExperimentStatus.FromString,
    ('experiment.ExperimentService', 'StopExperiment'): ExperimentStatus.FromString,
  }
  cardinalities = {
    'GetExperimentStatus': cardinality.Cardinality.UNARY_UNARY,
    'StartExperiment': cardinality.Cardinality.UNARY_UNARY,
    'StopExperiment': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'experiment.ExperimentService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
