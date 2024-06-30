from typing import Any

from pydantic import BaseModel, Field


class StaticParams(BaseModel):
    query: dict[str, Any] = Field(default_factory=dict)
    body: dict[str, Any] = Field(default_factory=dict)


class DynamicParams(BaseModel):
    path: list[str] = Field(default_factory=list)
    query: list[str] = Field(default_factory=list)
    body: list[str] = Field(default_factory=list)
