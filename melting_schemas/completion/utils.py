from typing import Annotated, Literal

from pydantic import BaseModel, Field

FinishReason = Literal["stop", "length", "function_call", "tool_calls"]


class ChatMLMessage(BaseModel):
    content: str
    name: Annotated[str, Field(regex=r"^[a-zA-Z0-9_]*$", max_length=64)] | None = None
    role: Literal["user", "assistant", "system"]


class ChatMLMessageChunk(BaseModel):
    finish_reason: FinishReason | None = None
    delta: str


class TemplateInputs(BaseModel):
    inputs: dict[str, str]
    name: Annotated[str, Field(regex=r"^[a-zA-Z0-9_]*$", max_length=64)] | None = None
    role: Literal["user", "system", "assistant"]
    template_name: str | None = None  # Advanced usage: select sub-templates


class Templating(BaseModel):
    prompt_inputs: list[TemplateInputs | dict]
    prompt_id: str
    prompt_name: str
