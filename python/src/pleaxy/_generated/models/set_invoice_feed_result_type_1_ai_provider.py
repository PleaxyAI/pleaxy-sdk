from typing import Literal, Set, cast

SetInvoiceFeedResultType1AiProvider = Literal[
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES: Set[
    SetInvoiceFeedResultType1AiProvider
] = {
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_set_invoice_feed_result_type_1_ai_provider(
    value: str,
) -> SetInvoiceFeedResultType1AiProvider:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES:
        return cast(SetInvoiceFeedResultType1AiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES!r}"
    )
