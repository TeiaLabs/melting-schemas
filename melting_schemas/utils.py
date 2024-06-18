from typing import Required, TypedDict


class Timings(TypedDict):
    total: float


class StreamTimings(TypedDict):
    avg: float
    first: float
    max: float
    min: float
    total: float


class TokenUsage(TypedDict, total=False):
    prompt_tokens: Required[int]
    total_tokens: Required[int]
    completion_tokens: int
