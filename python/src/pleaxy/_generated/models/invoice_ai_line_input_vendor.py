from typing import Literal, Set, cast

InvoiceAiLineInputVendor = Literal[
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

INVOICE_AI_LINE_INPUT_VENDOR_VALUES: Set[InvoiceAiLineInputVendor] = {
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


def check_invoice_ai_line_input_vendor(value: str) -> InvoiceAiLineInputVendor:
    if value in INVOICE_AI_LINE_INPUT_VENDOR_VALUES:
        return cast(InvoiceAiLineInputVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_AI_LINE_INPUT_VENDOR_VALUES!r}"
    )
