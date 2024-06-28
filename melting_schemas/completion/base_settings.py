from typing import Annotated

from pydantic import BaseModel, Field


class BaseModelSettings(BaseModel):
    model: str
    max_tokens: Annotated[int | None, Field(ge=1)] = None  # defaults to inf
    temperature: Annotated[float | None, Field(ge=0, le=2)] = None
    top_p: Annotated[float | None, Field(ge=0, le=1)] = None
    logit_bias: dict[str, Annotated[int, Field(ge=-100, le=100)]] | None = None
    stop: Annotated[list[str], Field(max_length=4)] | None = None
