from typing import Literal, Set, cast

AiPoLineSuggestionsInvoicer = Literal[
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

AI_PO_LINE_SUGGESTIONS_INVOICER_VALUES: Set[AiPoLineSuggestionsInvoicer] = {
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


def check_ai_po_line_suggestions_invoicer(value: str) -> AiPoLineSuggestionsInvoicer:
    if value in AI_PO_LINE_SUGGESTIONS_INVOICER_VALUES:
        return cast(AiPoLineSuggestionsInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTIONS_INVOICER_VALUES!r}"
    )
