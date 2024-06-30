from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.usage import StreamTimings, Timings, TokenUsage

from ..buffered_ml_messages import (
    ChatMLMessage,
    FunctionCallMLMessage,
    FunctionMLMessage,
)
from ..templating import Templating
from .settings import FCallModelSettings


class FCallCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length", "function_call"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage]
    output: ChatMLMessage | FunctionCallMLMessage | FunctionMLMessage
    settings: FCallModelSettings
    templating: Templating | None = None
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
