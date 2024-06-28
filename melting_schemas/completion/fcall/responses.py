from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.usage import StreamTimings, Timings, TokenUsage

from ..utils import ChatMLMessage, Templating
from .settings import FCallModelSettings
from .utils import FunctionCallMLMessage, FunctionMLMessage


class FCallCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length", "function_call"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage]
    output: ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage
    settings: FCallModelSettings
    templating: Optional[Templating]
    timings: Timings | StreamTimings
    usage: TokenUsage


class ToolStreamedResponse(BaseModel):
    op_type: Literal["step", "result", "start", "stop", "execution_id", "error", "selection"]
    tool_name: str | None = None
    method: str | None = None
    content: str


class StartToolStreamedResponse(ToolStreamedResponse):
    params: dict
    selection_id: str | None = None


class StopToolStreamedResponse(ToolStreamedResponse):
    response_time: float
    error: str | None = None
