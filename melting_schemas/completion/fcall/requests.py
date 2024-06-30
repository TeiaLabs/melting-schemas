from pydantic import BaseModel

from melting_schemas.json_schema import FunctionJsonSchema

from ..buffered_ml_messages import (
    ChatMLMessage,
    FunctionCallMLMessage,
    FunctionMLMessage,
)
from .settings import FCallModelSettings


class RawFCallRequest(BaseModel):
    functions: list[FunctionJsonSchema]
    messages: list[ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage]
    settings: FCallModelSettings
