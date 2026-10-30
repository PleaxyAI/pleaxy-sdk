from typing import Literal, Set, cast

AiPoLineSuggestionAiVendor = Literal[
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

AI_PO_LINE_SUGGESTION_AI_VENDOR_VALUES: Set[AiPoLineSuggestionAiVendor] = {
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


def check_ai_po_line_suggestion_ai_vendor(value: str) -> AiPoLineSuggestionAiVendor:
    if value in AI_PO_LINE_SUGGESTION_AI_VENDOR_VALUES:
        return cast(AiPoLineSuggestionAiVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PO_LINE_SUGGESTION_AI_VENDOR_VALUES!r}"
    )
