from typing import Optional

from kotaemon.base import Param


def get_model(type):
    types = {"embedding": "text-embedding-004", "chat": "gemini-1.5-flash"}
    return Param(
        f"models/{types.get(type)}",
        help=(
            f"The name of the required {type} model "
            "(https://ai.google.dev/gemini-api/docs/models/gemini). "
            "Must be in the format 'model/...'."
        ),
    )


class BaseGeminiModel:
    google_api_key: str = Param("", help="The API key received from Gemini.")


class BaseGeminiChatModel(BaseGeminiModel):
    model: str = get_model("chat")

    temperature: Optional[float] = Param(
        0.7,
        help="Run inference with this temperature. Must be between 0.0 and 1.0.",
    )

    top_k: Optional[float] = Param(
        None,
        help=(
            "Decode using top-k sampling by considering the set of "
            "top_k most probable tokens. Must be larger than 0."
        ),
    )

    top_p: Optional[float] = Param(
        None,
        help=(
            "Decode using nucleus samplingby considering the smallest set of "
            "tokens whose probability sum is at least top_p. "
            "Must be between 0.0 and 1.0."
        ),
    )

    max_output_tokens: Optional[float] = Param(
        None,
        help=(
            "Maximum number of tokens to include in a candidate. "
            "Must be greater than zero. If unset, will default to 64."
        ),
    )

    max_retries: Optional[float] = Param(
        None, help="The maximum number of retries to make when generating."
    )

    timeout: Optional[float] = Param(
        None, help="The maximum number of seconds to wait for a response."
    )
