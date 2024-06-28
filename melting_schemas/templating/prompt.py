from prompts import DynamicSchema, PromptRole, Template, TurboSchema
from prompts.schemas import TurboSchema
from pydantic import BaseModel, Field

from ..completion.chat import ChatModelSettings
from ..meta import Creator

# ====== Create Schemas ======


class ChatPromptTemplate(TurboSchema):
    settings: ChatModelSettings


class CreateCompletionPrompt(DynamicSchema):
    pass


# ====== Get Schemas ======


class GeneratedFields(BaseModel):
    created_at: str
    created_by: Creator
    id: str = Field(alias="_id")


class ChatPrompt(GeneratedFields, TurboSchema):
    pass


class GetCompletionPrompt(GeneratedFields, DynamicSchema):
    pass


# ====== Update Schemas ======


class UpdateChatTemplateData(BaseModel):
    name: str | None = None
    role: PromptRole | None = None
    replacements: dict[str, str] | None = None


class UpdateSettings(BaseModel):
    model: str | None = None
    max_tokens: int | None = None
    stop: list[str] | None = None
    temperature: float | None = None
    top_p: float | None = None
    frequency_penalty: float | None = None
    presence_penalty: float | None = None


class BaseUpdatePrompt(BaseModel):
    # Prompt fields
    description: str | None = None
    settings: UpdateSettings | None = None

    # Prompt start
    initial_template_data: str | list[UpdateChatTemplateData] | None = None


class UpdateChatPrompt(BaseUpdatePrompt):
    # Templates
    assistant_templates: list[Template] | None = None
    system_templates: list[Template] | None = None
    user_templates: list[Template] | None = None


class UpdateCompletionPrompt(BaseUpdatePrompt):
    # Template
    template: str | None = None
