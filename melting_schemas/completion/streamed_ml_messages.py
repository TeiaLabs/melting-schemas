from typing import Any, Literal

from pydantic import BaseModel

from .finish_reason import FinishReason


class ChatMLMessageChunk(BaseModel):
    finish_reason: FinishReason | None = None
    delta: str


class ToolCallFunctionChunk(BaseModel):
    delta: str
    name: str | None = None


class ToolCallChunk(BaseModel):
    id: str
    type: Literal["function"]
    function: ToolCallFunctionChunk


class ToolCallMLMessageChunk(BaseModel):
    finish_reason: FinishReason
    content: str
    tool_calls: list[ToolCallChunk]
    role: Literal["assistant"]


class ToolMLMessageChunk(BaseModel):
    id: Any
    delta: str
    name: str
    role: Literal["tool"]
