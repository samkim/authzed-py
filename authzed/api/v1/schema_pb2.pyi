"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ReadSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___ReadSchemaRequest = ReadSchemaRequest

class ReadSchemaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCHEMA_TEXT_FIELD_NUMBER: builtins.int
    schema_text: typing.Text = ...

    def __init__(self,
        *,
        schema_text : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"schema_text",b"schema_text"]) -> None: ...
global___ReadSchemaResponse = ReadSchemaResponse

class WriteSchemaRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SCHEMA_FIELD_NUMBER: builtins.int
    schema: typing.Text = ...

    def __init__(self,
        *,
        schema : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"schema",b"schema"]) -> None: ...
global___WriteSchemaRequest = WriteSchemaRequest

class WriteSchemaResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___WriteSchemaResponse = WriteSchemaResponse
