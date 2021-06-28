# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authzed.api.v0 import developer_pb2 as authzed_dot_api_dot_v0_dot_developer__pb2


class DeveloperServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EditCheck = channel.unary_unary(
                '/authzed.api.v0.DeveloperService/EditCheck',
                request_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckResponse.FromString,
                )
        self.Validate = channel.unary_unary(
                '/authzed.api.v0.DeveloperService/Validate',
                request_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.ValidateRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.ValidateResponse.FromString,
                )
        self.Share = channel.unary_unary(
                '/authzed.api.v0.DeveloperService/Share',
                request_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.ShareRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.ShareResponse.FromString,
                )
        self.LookupShared = channel.unary_unary(
                '/authzed.api.v0.DeveloperService/LookupShared',
                request_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareResponse.FromString,
                )


class DeveloperServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EditCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Validate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Share(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupShared(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeveloperServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EditCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.EditCheck,
                    request_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckResponse.SerializeToString,
            ),
            'Validate': grpc.unary_unary_rpc_method_handler(
                    servicer.Validate,
                    request_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.ValidateRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.ValidateResponse.SerializeToString,
            ),
            'Share': grpc.unary_unary_rpc_method_handler(
                    servicer.Share,
                    request_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.ShareRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.ShareResponse.SerializeToString,
            ),
            'LookupShared': grpc.unary_unary_rpc_method_handler(
                    servicer.LookupShared,
                    request_deserializer=authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authzed.api.v0.DeveloperService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeveloperService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EditCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v0.DeveloperService/EditCheck',
            authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckRequest.SerializeToString,
            authzed_dot_api_dot_v0_dot_developer__pb2.EditCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Validate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v0.DeveloperService/Validate',
            authzed_dot_api_dot_v0_dot_developer__pb2.ValidateRequest.SerializeToString,
            authzed_dot_api_dot_v0_dot_developer__pb2.ValidateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Share(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v0.DeveloperService/Share',
            authzed_dot_api_dot_v0_dot_developer__pb2.ShareRequest.SerializeToString,
            authzed_dot_api_dot_v0_dot_developer__pb2.ShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupShared(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v0.DeveloperService/LookupShared',
            authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareRequest.SerializeToString,
            authzed_dot_api_dot_v0_dot_developer__pb2.LookupShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
