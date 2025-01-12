"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v0.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class WatchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACES_FIELD_NUMBER: builtins.int
    START_REVISION_FIELD_NUMBER: builtins.int

    @property
    def namespaces(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...

    @property
    def start_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        namespaces : typing.Optional[typing.Iterable[typing.Text]] = ...,
        start_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"start_revision",b"start_revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespaces",b"namespaces",u"start_revision",b"start_revision"]) -> None: ...
global___WatchRequest = WatchRequest

class WatchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATES_FIELD_NUMBER: builtins.int
    END_REVISION_FIELD_NUMBER: builtins.int

    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v0.core_pb2.RelationTupleUpdate]: ...

    @property
    def end_revision(self) -> authzed.api.v0.core_pb2.Zookie: ...

    def __init__(self,
        *,
        updates : typing.Optional[typing.Iterable[authzed.api.v0.core_pb2.RelationTupleUpdate]] = ...,
        end_revision : typing.Optional[authzed.api.v0.core_pb2.Zookie] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"end_revision",b"end_revision"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"end_revision",b"end_revision",u"updates",b"updates"]) -> None: ...
global___WatchResponse = WatchResponse
