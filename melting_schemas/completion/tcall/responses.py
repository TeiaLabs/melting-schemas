import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..usage import StreamTimings, Timings, TokenUsage

class TCallCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length", "function_call", "tool_calls"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    tool_calls: list[ToolCall]
    output: ChatMLMessage | ToolMLMessage | ToolCallMLMessage
    settings: ChatModelSettings
    templating: Optional[Templating]
    timings: Timings | StreamTimings
    usage: TokenUsage

    class Config:
        smart_unions = True
