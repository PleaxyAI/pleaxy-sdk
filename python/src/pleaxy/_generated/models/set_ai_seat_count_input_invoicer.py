from typing import Literal, Set, cast

SetAiSeatCountInputInvoicer = Literal[
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "gcp",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

SET_AI_SEAT_COUNT_INPUT_INVOICER_VALUES: Set[SetAiSeatCountInputInvoicer] = {
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "gcp",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_set_ai_seat_count_input_invoicer(value: str) -> SetAiSeatCountInputInvoicer:
    if value in SET_AI_SEAT_COUNT_INPUT_INVOICER_VALUES:
        return cast(SetAiSeatCountInputInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_AI_SEAT_COUNT_INPUT_INVOICER_VALUES!r}"
    )
