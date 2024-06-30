from datetime import datetime

from pydantic import BaseModel, Field

from ..meta import Creator
from ..usage import TokenUsage


class TextEncodingResponse(BaseModel):
    id: str = Field(..., alias="_id")
    created_at: datetime
    created_by: Creator
    model: str
    usage: TokenUsage | None = None
    vectors: list[list[float]]


class RawTextEncoding(BaseModel):
    snippets: list[str]
    model: str
