import datetime
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.usage import StreamTimings, Timings, TokenUsage

from ..buffered_ml_messages import (
    BufferedMLMessageType,
    ChatMLMessage,
    ToolCallMLMessage,
)
from ..finish_reason import FinishReason
from ..templating import Templating
from .settings import TCallModelSettings
from .specs import FunctionJsonSchema, ToolSpec


class ToolInfo(BaseModel):
    spec: ToolSpec | FunctionJsonSchema  # Snapshot of the tool spec or JsonSchema
    selected: bool  # If it was selected or not
    ml_message_id: Any = None  # identifier of the message that triggered it


class TCallResponse(BaseModel):
    id: Any = Field(alias="_id")

    # Execution
    finish_reason: FinishReason
    start_messages: list[BufferedMLMessageType]  # Messages passed by user or built from prompt
    generated_messages: list[BufferedMLMessageType]  # Messages generated from the execution
    tools: list[ToolInfo]
    output: ChatMLMessage | ToolCallMLMessage  # Last message generated
    templating: Templating | None = None

    settings: TCallModelSettings
    timings: Timings | StreamTimings
    usage: TokenUsage

    # Metadata
    created_at: datetime
    created_by: Creator
