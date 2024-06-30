from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from ..completion.text import TextModelSettings
from ..meta import Creator
from ..usage import Timings, TokenUsage


class TextCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length"]
    id: str = Field(..., alias="_id")
    text: str
    suffix: str | None = None
    output: str
    settings: TextModelSettings
    timings: Timings
    usage: TokenUsage


class RawTextCompletionRequest(BaseModel):
    text: str
    settings: TextModelSettings
    suffix: str | None = None
