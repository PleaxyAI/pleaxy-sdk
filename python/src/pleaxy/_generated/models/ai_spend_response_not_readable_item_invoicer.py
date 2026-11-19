from typing import Literal, Set, cast

AiSpendResponseNotReadableItemInvoicer = Literal[
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

AI_SPEND_RESPONSE_NOT_READABLE_ITEM_INVOICER_VALUES: Set[
    AiSpendResponseNotReadableItemInvoicer
] = {
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


def check_ai_spend_response_not_readable_item_invoicer(
    value: str,
) -> AiSpendResponseNotReadableItemInvoicer:
    if value in AI_SPEND_RESPONSE_NOT_READABLE_ITEM_INVOICER_VALUES:
        return cast(AiSpendResponseNotReadableItemInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_RESPONSE_NOT_READABLE_ITEM_INVOICER_VALUES!r}"
    )
