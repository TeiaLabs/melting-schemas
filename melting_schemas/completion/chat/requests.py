from typing import Optional

from pydantic import BaseModel

from ..utils import ChatMLMessage, TemplateInputs
from .settings import ChatModelSettings


class RawChatCompletionRequest(BaseModel):
    history: str | None = None
    messages: list[ChatMLMessage]
    settings: ChatModelSettings


class ChatCompletionRequest(BaseModel):
    history: str | None = None
    prompt_inputs: list[TemplateInputs]
    prompt_name: str
    settings: Optional[ChatModelSettings] = None


class HybridChatCompletionRequest(BaseModel):
    history: str | None = None
    prompt_name: str
    messages: list[ChatMLMessage | TemplateInputs]
    settings: Optional[ChatModelSettings] = None
