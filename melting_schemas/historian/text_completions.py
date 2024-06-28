from datetime import datetime
from typing import Literal, Optional

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
    suffix: Optional[str]
    output: str
    settings: TextModelSettings
    timings: Timings
    usage: TokenUsage


class RawTextCompletionRequest(BaseModel):
    text: str
    settings: TextModelSettings
    suffix: Optional[str] = None
