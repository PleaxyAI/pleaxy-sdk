from typing import Literal, Set, cast

AiSeatCountInvoicer = Literal[
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
]

AI_SEAT_COUNT_INVOICER_VALUES: Set[AiSeatCountInvoicer] = {
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
}


def check_ai_seat_count_invoicer(value: str) -> AiSeatCountInvoicer:
    if value in AI_SEAT_COUNT_INVOICER_VALUES:
        return cast(AiSeatCountInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SEAT_COUNT_INVOICER_VALUES!r}"
    )
