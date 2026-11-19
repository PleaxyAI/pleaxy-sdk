from typing import Literal, Set, cast

AiPoLineSuggestionAiInvoicer = Literal[
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

AI_PO_LINE_SUGGESTION_AI_INVOICER_VALUES: Set[AiPoLineSuggestionAiInvoicer] = {
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


def check_ai_po_line_suggestion_ai_invoicer(value: str) -> AiPoLineSuggestionAiInvoicer:
    if value in AI_PO_LINE_SUGGESTION_AI_INVOICER_VALUES:
        return cast(AiPoLineSuggestionAiInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTION_AI_INVOICER_VALUES!r}"
    )
