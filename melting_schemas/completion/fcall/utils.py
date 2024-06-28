from typing import Annotated, Literal

from pydantic import BaseModel, Field


class FunctionCall(BaseModel):
    name: Annotated[str, Field(regex=r"^[a-zA-Z0-9_]*$", max_length=64)]
    arguments: str


class FunctionCallMLMessage(BaseModel):
    content: str | None = None
    function_call: FunctionCall
    role: Literal["assistant"] = "assistant"


class FunctionMLMessage(BaseModel):
    content: str
    name: Annotated[str, Field(regex=r"^[a-zA-Z0-9_]*$", max_length=64)] | None = None
    role: Literal["function"] = "function"
