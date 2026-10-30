from typing import Literal, Set, cast

AiRateCardEntryInvoicer = Literal[
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

AI_RATE_CARD_ENTRY_INVOICER_VALUES: Set[AiRateCardEntryInvoicer] = {
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


def check_ai_rate_card_entry_invoicer(value: str) -> AiRateCardEntryInvoicer:
    if value in AI_RATE_CARD_ENTRY_INVOICER_VALUES:
        return cast(AiRateCardEntryInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_RATE_CARD_ENTRY_INVOICER_VALUES!r}"
    )
