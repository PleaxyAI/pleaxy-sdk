from typing import Literal, Set, cast

AiUncoveredSpendInvoicer = Literal[
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

AI_UNCOVERED_SPEND_INVOICER_VALUES: Set[AiUncoveredSpendInvoicer] = {
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


def check_ai_uncovered_spend_invoicer(value: str) -> AiUncoveredSpendInvoicer:
    if value in AI_UNCOVERED_SPEND_INVOICER_VALUES:
        return cast(AiUncoveredSpendInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_UNCOVERED_SPEND_INVOICER_VALUES!r}"
    )
