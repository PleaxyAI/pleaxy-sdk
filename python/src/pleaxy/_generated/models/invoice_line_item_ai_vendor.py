from typing import Literal, Set, cast

InvoiceLineItemAiVendor = Literal[
    "amazon",
    "anthropic",
    "cohere",
    "databricks",
    "deepseek",
    "google",
    "meta",
    "microsoft",
    "mistral",
    "nvidia",
    "openai",
    "snowflake",
    "unknown",
    "xai",
]

INVOICE_LINE_ITEM_AI_VENDOR_VALUES: Set[InvoiceLineItemAiVendor] = {
    "amazon",
    "anthropic",
    "cohere",
    "databricks",
    "deepseek",
    "google",
    "meta",
    "microsoft",
    "mistral",
    "nvidia",
    "openai",
    "snowflake",
    "unknown",
    "xai",
}


def check_invoice_line_item_ai_vendor(value: str) -> InvoiceLineItemAiVendor:
    if value in INVOICE_LINE_ITEM_AI_VENDOR_VALUES:
        return cast(InvoiceLineItemAiVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_LINE_ITEM_AI_VENDOR_VALUES!r}"
    )
