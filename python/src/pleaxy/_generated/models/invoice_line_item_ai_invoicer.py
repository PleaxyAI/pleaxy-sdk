from typing import Literal, Set, cast

InvoiceLineItemAiInvoicer = Literal[
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

INVOICE_LINE_ITEM_AI_INVOICER_VALUES: Set[InvoiceLineItemAiInvoicer] = {
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


def check_invoice_line_item_ai_invoicer(value: str) -> InvoiceLineItemAiInvoicer:
    if value in INVOICE_LINE_ITEM_AI_INVOICER_VALUES:
        return cast(InvoiceLineItemAiInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_LINE_ITEM_AI_INVOICER_VALUES!r}"
    )
