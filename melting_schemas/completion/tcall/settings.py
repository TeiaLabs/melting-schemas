import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..usage import StreamTimings, Timings, TokenUsage

class TCallModelSettings(BaseModel):
    model: str
    max_iterations: int = 10  # Maximum back and fourth allowed
    max_tokens: int | None = None  # defaults to inf
    temperature: float | None = None  # ValueRange(0, 2)
    top_p: float | None = None  # ValueRange(0, 1)
    frequency_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    presence_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    logit_bias: dict[str, int] | None = None  # valmap(ValueRange(-100, 100))
    stop: list[str] | None = None  # MaxLen(4)
    tool_choice: Literal["auto", "required"] = "auto"  # defaults to auto
