import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from melting_schemas.meta import Creator
from melting_schemas.utils import StreamTimings, Timings

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..utils import TokenUsage


class TCallModelSettings(BaseModel):
    model: str
    max_iterations: int = 5  # Maximum back and fourth allowed
    max_tokens: int | None = None  # defaults to inf
    temperature: float | None = None  # ValueRange(0, 2)
    top_p: float | None = None  # ValueRange(0, 1)
    frequency_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    presence_penalty: float | None = None  # ValueRange(-2, 2) defaults to 0
    logit_bias: dict[str, int] | None = None  # valmap(ValueRange(-100, 100))
    stop: list[str] | None = None  # MaxLen(4)
    tool_choice: Literal["auto", "required"] = "auto"  # defaults to auto


class ToolCall(TypedDict):
    id: str
    name: str
    arguments: str
    extra: NotRequired[dict[str, str]]


class ToolCallMLMessage(TypedDict):
    content: Optional[None]
    tool_call: list[ToolCall]
    role: Literal["assistant"]


class ToolMLMessage(TypedDict):
    content: str
    name: str
    role: Literal["tool"]


class ToolJsonSchema(BaseModel):
    type: Literal["function"] = "function"
    function: FunctionJsonSchema


class RawTCallRequest(BaseModel):
    tools: list[ToolJsonSchema]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings

    class Config:
        smart_unions = True
        examples = {
            "Tool calling": {
                "tools": [
                    {
                        "type": "function",
                        "function": {
                            "name": "my_function",
                            "description": "This is my function",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "my_param": {
                                        "type": "string",
                                        "description": "This is my parameter",
                                    }
                                },
                                "required": ["my_param"],
                            },
                        },
                    }
                ],
                "messages": [
                    {
                        "content": "Hello",
                        "role": "user",
                    },
                    {
                        "content": "my_function",
                        "function_call": {
                            "name": "my_function",
                            "arguments": '{"my_param": "my_value"}',
                        },
                        "role": "assistant",
                    },
                ],
                "tool_choice": "auto",
            }
        }


class NativeTCallRequest(BaseModel):
    tools: list[str]
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    settings: TCallModelSettings

    class Config:
        smart_unions = True
        examples = {
            "Tool calling": {
                "tools": ["example-tool-name"],
                "messages": [
                    {
                        "content": "Hello",
                        "role": "user",
                    }
                ],
            }
        }


class TCallCompletionCreationResponse(BaseModel):
    created_at: datetime
    created_by: Creator
    finish_reason: Literal["stop", "length", "function_call", "tool_calls"]
    id: str = Field(..., alias="_id")
    messages: list[ChatMLMessage | ToolCallMLMessage | ToolMLMessage]
    output: ChatMLMessage | ToolMLMessage | ToolCallMLMessage
    settings: ChatModelSettings
    templating: Optional[Templating]
    timings: Timings | StreamTimings
    usage: TokenUsage

    class Config:
        smart_unions = True


class StaticParams(BaseModel):
    query: dict[str, Any] = Field(default_factory=dict)
    body: dict[str, Any] = Field(default_factory=dict)


class DynamicParams(BaseModel):
    path: list[str] = Field(default_factory=list)
    query: list[str] = Field(default_factory=list)
    body: list[str] = Field(default_factory=list)


class ToolArgMap(BaseModel):
    location: str
    name: str


class HttpToolCallee(BaseModel):
    type: Literal["http"] = "http"
    method: Literal["GET", "POST"]
    forward_headers: list[str] = Field(alias="forward-headers", default_factory=list)
    headers: dict[str, str] = Field(default_factory=dict)
    url: str
    static: StaticParams = Field(default_factory=StaticParams)
    dynamic: DynamicParams = Field(default_factory=DynamicParams)


class NoopToolCallee(BaseModel):
    type: Literal["noop"] = "noop"


class ToolSpec(BaseModel):
    name: str
    callee: HttpToolCallee | NoopToolCallee
    json_schema: ToolJsonSchema
