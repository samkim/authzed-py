"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .schema_pb2 import *
class SchemaServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    ReadSchema:grpc.UnaryUnaryMultiCallable[
        global___ReadSchemaRequest,
        global___ReadSchemaResponse] = ...

    WriteSchema:grpc.UnaryUnaryMultiCallable[
        global___WriteSchemaRequest,
        global___WriteSchemaResponse] = ...


class SchemaServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ReadSchema(self,
        request: global___ReadSchemaRequest,
        context: grpc.ServicerContext,
    ) -> global___ReadSchemaResponse: ...

    @abc.abstractmethod
    def WriteSchema(self,
        request: global___WriteSchemaRequest,
        context: grpc.ServicerContext,
    ) -> global___WriteSchemaResponse: ...


def add_SchemaServiceServicer_to_server(servicer: SchemaServiceServicer, server: grpc.Server) -> None: ...
