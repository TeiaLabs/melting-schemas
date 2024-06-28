from melting_schemas.json_schema import FunctionJsonSchema, ObjectSchema, StringSchema
from melting_schemas.utils import wrap

from .requests import ChatMLMessage, RawFCallRequest
from .settings import FCallModelSettings
from .utils import FunctionCall, FunctionCallMLMessage, FunctionMLMessage


def raw_fcall_request_examples():
    function_calling = RawFCallRequest(
        messages=[
            ChatMLMessage(content="What is the weather like in Boston?", role="user"),
        ],
        functions=[
            FunctionJsonSchema(
                name="get_current_weather",
                description="Get the current weather in a given location",
                parameters=ObjectSchema(
                    type="object",
                    properties={
                        "location": StringSchema(
                            type="string",
                            description="The city and state, e.g. San Francisco, CA",
                        ),
                    },
                    required=["location"],
                ),
            )
        ],
        settings=FCallModelSettings(model="gpt-3.5-turbo-0613"),
    )

    function_completion = RawFCallRequest(
        messages=[
            ChatMLMessage(
                content="What is the weather like in Boston?",
                role="user",
            ),
            FunctionCallMLMessage(
                function_call=FunctionCall(
                    name="get_current_weather",
                    arguments='{"location": "Boston, MA"}',
                ),
                role="assistant",
            ),
            FunctionMLMessage(
                content='{"temperature": "22", "unit": "celsius", "description": "Sunny"}',
                name="get_current_weather",
                role="function",
            ),
        ],
        functions=[
            FunctionJsonSchema(
                name="get_current_weather",
                description="Get the current weather in a given location",
                parameters=ObjectSchema(
                    type="object",
                    properties={
                        "location": StringSchema(
                            type="string",
                            description="The city and state, e.g. San Francisco, CA",
                        ),
                    },
                    required=["location"],
                ),
            )
        ],
        settings=FCallModelSettings(model="gpt-3.5-turbo-0613"),
    )

    return [
        wrap(name="Function calling", value=function_calling),
        wrap(name="Function completion", value=function_completion),
    ]
