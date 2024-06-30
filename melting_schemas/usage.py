from typing import NotRequired, TypedDict

from .completion.finish_reason import FinishReason


class TokenUsage(TypedDict):
    prompt_tokens: int
    total_tokens: int
    completion_tokens: NotRequired[int]


class Timings(TypedDict):
    total: float


class StreamTimings(TypedDict):
    avg: float
    first: float
    max: float
    min: float
    total: float


class StreamUsageInfo(TypedDict):
    finish_reason: NotRequired[FinishReason]
    token_usage: TokenUsage
    timings: StreamTimings
