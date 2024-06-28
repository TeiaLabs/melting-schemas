from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.usage import StreamTimings, Timings, TokenUsage

from ..utils import ChatMLMessage, Templating
from .settings import ChatModelSettings


class ChatCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage]
    output: ChatMLMessage
    settings: ChatModelSettings
    templating: Optional[Templating]
    timings: Timings | StreamTimings
    usage: TokenUsage


class StreamedChatCompletionCreationResponse(BaseModel):
    finish_reason: Literal["stop", "length"] | None = None
    delta: str
    acc_usage: TokenUsage
