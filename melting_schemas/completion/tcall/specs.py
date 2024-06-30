from typing import Literal

from pydantic import BaseModel, Field

from melting_schemas.json_schema import FunctionJsonSchema

from .params import DynamicParams, StaticParams


class NoopToolCallee(BaseModel):
    type: Literal["noop"] = "noop"


class HttpToolCallee(BaseModel):
    type: Literal["http"] = "http"
    method: Literal["GET", "POST"]
    forward_headers: list[str] = Field(default_factory=list)
    headers: dict[str, str] = Field(default_factory=dict)
    url: str
    static: StaticParams = Field(default_factory=StaticParams)
    dynamic: DynamicParams = Field(default_factory=DynamicParams)
    argument_map: dict[str, str] = Field(default_factory=dict)


class ToolJsonSchema(BaseModel):
    type: Literal["function"] = "function"
    function: FunctionJsonSchema


class ToolSpec(BaseModel):
    tool_name: str
    callee: HttpToolCallee | NoopToolCallee
    json_schema: ToolJsonSchema
