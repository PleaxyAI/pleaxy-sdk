from typing import Literal, Set, cast

SetInvoiceFeedResultType1AiProvider = Literal[
    "anthropic",
    "cohere",
    "confluent",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "datadog",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "mongodb",
    "nebius",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "twilio",
    "vercel",
    "xai",
    "zoom",
]

SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES: Set[
    SetInvoiceFeedResultType1AiProvider
] = {
    "anthropic",
    "cohere",
    "confluent",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "datadog",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "mongodb",
    "nebius",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "twilio",
    "vercel",
    "xai",
    "zoom",
}


def check_set_invoice_feed_result_type_1_ai_provider(
    value: str,
) -> SetInvoiceFeedResultType1AiProvider:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES:
        return cast(SetInvoiceFeedResultType1AiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_AI_PROVIDER_VALUES!r}"
    )
