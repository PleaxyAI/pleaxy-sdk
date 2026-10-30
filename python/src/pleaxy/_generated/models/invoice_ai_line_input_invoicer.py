from typing import Literal, Set, cast

InvoiceAiLineInputInvoicer = Literal[
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "gcp",
    "lambda",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

INVOICE_AI_LINE_INPUT_INVOICER_VALUES: Set[InvoiceAiLineInputInvoicer] = {
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "gcp",
    "lambda",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_invoice_ai_line_input_invoicer(value: str) -> InvoiceAiLineInputInvoicer:
    if value in INVOICE_AI_LINE_INPUT_INVOICER_VALUES:
        return cast(InvoiceAiLineInputInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_AI_LINE_INPUT_INVOICER_VALUES!r}"
    )
