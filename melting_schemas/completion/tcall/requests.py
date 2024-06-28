import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..usage import StreamTimings, Timings, TokenUsage


class TCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings

    


class TCallProcessedRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings
