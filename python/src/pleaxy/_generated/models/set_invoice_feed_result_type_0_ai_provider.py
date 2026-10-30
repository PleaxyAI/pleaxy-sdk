from typing import Literal, Set, cast

SetInvoiceFeedResultType0AiProvider = Literal[
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "lambda",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

SET_INVOICE_FEED_RESULT_TYPE_0_AI_PROVIDER_VALUES: Set[
    SetInvoiceFeedResultType0AiProvider
] = {
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "lambda",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_set_invoice_feed_result_type_0_ai_provider(
    value: str,
) -> SetInvoiceFeedResultType0AiProvider:
    if value in SET_INVOICE_FEED_RESULT_TYPE_0_AI_PROVIDER_VALUES:
        return cast(SetInvoiceFeedResultType0AiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_0_AI_PROVIDER_VALUES!r}"
    )
