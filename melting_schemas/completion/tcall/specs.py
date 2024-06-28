import datetime
from datetime import datetime
from typing import Any, Literal, NotRequired, Optional, TypedDict

from pydantic import BaseModel, Field

from ..completion.chat import ChatMLMessage, ChatModelSettings, Templating
from ..json_schema import FunctionJsonSchema
from ..meta import Creator
from ..usage import StreamTimings, Timings, TokenUsage


class ToolJsonSchema(BaseModel):
    type: Literal["function"] = "function"
    function: FunctionJsonSchema


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
    forward_headers: list[str] = Field(default_factory=list)
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

