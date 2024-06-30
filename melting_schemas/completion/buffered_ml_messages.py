from typing import Annotated, Any, Literal

from pydantic import BaseModel, Field


class ChatMLMessage(BaseModel):
    content: str
    name: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_]*$", max_length=64)] | None = None
    role: Literal["user", "assistant", "system"]


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


class FunctionCall(BaseModel):
    name: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_]*$", max_length=64)]
    arguments: str


class FunctionCallMLMessage(BaseModel):
    content: str | None = None
    function_call: FunctionCall
    role: Literal["assistant"] = "assistant"


class FunctionMLMessage(BaseModel):
    content: str
    name: Annotated[str, Field(pattern=r"^[a-zA-Z0-9_]*$", max_length=64)] | None = None
    role: Literal["function"] = "function"


BufferedMLMessageType = (
    ChatMLMessage | ToolCallMLMessage | ToolMLMessage | FunctionCallMLMessage | FunctionMLMessage
)
