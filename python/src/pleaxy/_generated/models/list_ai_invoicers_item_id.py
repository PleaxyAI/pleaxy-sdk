from typing import Literal, Set, cast

ListAiInvoicersItemId = Literal[
    "anthropic",
    "cohere",
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
    "xai",
    "zoom",
]

LIST_AI_INVOICERS_ITEM_ID_VALUES: Set[ListAiInvoicersItemId] = {
    "anthropic",
    "cohere",
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
    "xai",
    "zoom",
}


def check_list_ai_invoicers_item_id(value: str) -> ListAiInvoicersItemId:
    if value in LIST_AI_INVOICERS_ITEM_ID_VALUES:
        return cast(ListAiInvoicersItemId, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_ID_VALUES!r}"
    )
