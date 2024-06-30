from pydantic import BaseModel

from ..buffered_ml_messages import ChatMLMessage
from ..templating import TemplateInputs
from .settings import ChatModelSettings


class RawChatCompletionRequest(BaseModel):
    history: str | None = None
    messages: list[ChatMLMessage]
    settings: ChatModelSettings


class ChatCompletionRequest(BaseModel):
    history: str | None = None
    prompt_inputs: list[TemplateInputs]
    prompt_name: str
    settings: ChatModelSettings | None = None


class HybridChatCompletionRequest(BaseModel):
    history: str | None = None
    prompt_name: str
    messages: list[ChatMLMessage | TemplateInputs]
    settings: ChatModelSettings | None = None
