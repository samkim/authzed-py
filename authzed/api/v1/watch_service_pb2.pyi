"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class WatchRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OPTIONAL_OBJECT_TYPES_FIELD_NUMBER: builtins.int
    OPTIONAL_START_CURSOR_FIELD_NUMBER: builtins.int

    @property
    def optional_object_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...

    @property
    def optional_start_cursor(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        optional_object_types : typing.Optional[typing.Iterable[typing.Text]] = ...,
        optional_start_cursor : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"optional_start_cursor",b"optional_start_cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_object_types",b"optional_object_types",u"optional_start_cursor",b"optional_start_cursor"]) -> None: ...
global___WatchRequest = WatchRequest

class WatchResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATES_FIELD_NUMBER: builtins.int
    CHANGES_THROUGH_FIELD_NUMBER: builtins.int

    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[authzed.api.v1.core_pb2.RelationshipUpdate]: ...

    @property
    def changes_through(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        updates : typing.Optional[typing.Iterable[authzed.api.v1.core_pb2.RelationshipUpdate]] = ...,
        changes_through : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"changes_through",b"changes_through"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"changes_through",b"changes_through",u"updates",b"updates"]) -> None: ...
global___WatchResponse = WatchResponse
