from ..base_settings import BaseModelSettings


class TextModelSettings(BaseModelSettings):
    """
    Change these settings to tweak the model's behavior.

    Heavily inspired by https://platform.openai.com/docs/api-reference/completions/create
    """

    n: int = 1
