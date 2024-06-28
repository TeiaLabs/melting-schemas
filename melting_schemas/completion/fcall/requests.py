from pydantic import BaseModel

from melting_schemas.json_schema import FunctionJsonSchema

from ..utils import ChatMLMessage
from .settings import FCallModelSettings
from .utils import FunctionCallMLMessage, FunctionMLMessage


class RawFCallRequest(BaseModel):
    functions: list[FunctionJsonSchema]
    messages: list[ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage]
    settings: FCallModelSettings
