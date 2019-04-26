# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import select_pb2 as select__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SelectDatabase = channel.unary_unary(
        '/select.Greeter/SelectDatabase',
        request_serializer=select__pb2.SelectRequest.SerializeToString,
        response_deserializer=select__pb2.SelectReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def SelectDatabase(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SelectDatabase': grpc.unary_unary_rpc_method_handler(
          servicer.SelectDatabase,
          request_deserializer=select__pb2.SelectRequest.FromString,
          response_serializer=select__pb2.SelectReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'select.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
