# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authzed.api.v1 import permission_service_pb2 as authzed_dot_api_dot_v1_dot_permission__service__pb2


class PermissionsServiceStub(object):
    """PermissionsService is used to perform permissions and relationship
    operations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadRelationships = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/ReadRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.FromString,
                )
        self.WriteRelationships = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/WriteRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.FromString,
                )
        self.DeleteRelationships = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/DeleteRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.FromString,
                )
        self.CheckPermission = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/CheckPermission',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.FromString,
                )
        self.ExpandPermissionTree = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/ExpandPermissionTree',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.FromString,
                )
        self.LookupResources = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/LookupResources',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.FromString,
                )


class PermissionsServiceServicer(object):
    """PermissionsService is used to perform permissions and relationship
    operations.
    """

    def ReadRelationships(self, request, context):
        """ReadRelationships reads a set of the relationships matching one or more
        filters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteRelationships(self, request, context):
        """WriteRelationships writes and/or deletes a set of specified relationships,
        with an optional set of precondition relationships that must exist before
        the operation can commit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRelationships(self, request, context):
        """DeleteRelationships deletes relationships matching one or more filters, in
        bulk.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckPermission(self, request, context):
        """CheckPermission checks whether a subject has a particular permission or is
        a member of a particular relation, on a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandPermissionTree(self, request, context):
        """ExpandPermissionTree expands the relationships reachable from a particular
        permission or relation of a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupResources(self, request, context):
        """LookupResources returns the IDs of all resources on which the specified
        subject has permission or on which the specified subject is a member of the
        relation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PermissionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadRelationships': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.SerializeToString,
            ),
            'WriteRelationships': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.SerializeToString,
            ),
            'DeleteRelationships': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.SerializeToString,
            ),
            'CheckPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckPermission,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.SerializeToString,
            ),
            'ExpandPermissionTree': grpc.unary_unary_rpc_method_handler(
                    servicer.ExpandPermissionTree,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.SerializeToString,
            ),
            'LookupResources': grpc.unary_stream_rpc_method_handler(
                    servicer.LookupResources,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authzed.api.v1.PermissionsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PermissionsService(object):
    """PermissionsService is used to perform permissions and relationship
    operations.
    """

    @staticmethod
    def ReadRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/ReadRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/WriteRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/DeleteRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/CheckPermission',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandPermissionTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/ExpandPermissionTree',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/LookupResources',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
