from pydantic import BaseModel

from ..buffered_ml_messages import BufferedMLMessageType
from ..templating import TemplateInputs
from .settings import TCallModelSettings
from .specs import ToolJsonSchema, ToolSpec


class RawTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    messages: list[BufferedMLMessageType]

    settings: TCallModelSettings


class PromptedTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    prompt_inputs: list[TemplateInputs]
    prompt_name: str
    settings: TCallModelSettings | None = None


class HybridTCallRequest(BaseModel):
    tools: list[ToolSpec] | list[ToolJsonSchema] | list[str]
    messages: list[BufferedMLMessageType]

    prompt_inputs: list[TemplateInputs]
    prompt_name: str

    settings: TCallModelSettings | None = None
