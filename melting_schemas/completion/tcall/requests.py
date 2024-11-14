from pydantic import BaseModel, Field

from ..buffered_ml_messages import BufferedMLMessageType
from ..templating import TemplateInputs
from .params import StaticTool
from .settings import TCallModelSettings
from .specs import TollSpecOverride, ToolJsonSchema, ToolSpec


class RawTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str] = Field(
        default_factory=list
    )
    static_tools: list[StaticTool] = Field(default_factory=list)
    tool_overridings: dict[str, list[TollSpecOverride]] = Field(default_factory=dict)
    messages: list[BufferedMLMessageType]

    settings: TCallModelSettings


class PromptedTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str] = Field(
        default_factory=list
    )
    static_tools: list[StaticTool] = Field(default_factory=list)
    tool_overridings: dict[str, list[TollSpecOverride]] = Field(default_factory=dict)
    prompt_inputs: list[TemplateInputs]
    prompt_name: str
    settings: TCallModelSettings | None = None


class HybridTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str] = Field(
        default_factory=list
    )
    static_tools: list[StaticTool] = Field(default_factory=list)
    tool_overridings: dict[str, list[TollSpecOverride]] = Field(default_factory=dict)

    messages: list[BufferedMLMessageType]

    prompt_inputs: list[TemplateInputs]
    prompt_name: str

    settings: TCallModelSettings | None = None
