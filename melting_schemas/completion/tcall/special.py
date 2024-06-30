from typing import Any

from pydantic import BaseModel, Field

from ..buffered_ml_messages import BufferedMLMessageType
from .settings import TCallModelSettings
from .specs import ToolJsonSchema, ToolSpec


class StaticTool(BaseModel):
    name: str
    arguments: dict[str, str] = Field(default_factory=dict)
    response: Any


class SpecialTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    messages: list[BufferedMLMessageType]
    static_tools: list

    settings: TCallModelSettings
