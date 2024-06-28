from typing import Any, Literal

from pydantic import BaseModel

from ..utils import FinishReason

# Buffered


class ToolCallFunction(BaseModel):
    arguments: str
    name: str


class ToolCall(BaseModel):
    id: str
    type: Literal["function"]
    function: ToolCallFunction


class ToolCallMLMessage(BaseModel):
    content: str
    tool_calls: list[ToolCall]
    role: Literal["assistant"]


class ToolMLMessage(BaseModel):
    id: Any
    content: str
    name: str
    role: Literal["tool"]


# Streamed


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
