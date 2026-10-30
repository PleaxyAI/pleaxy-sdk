from typing import Literal, Set, cast

AiLineScopeInputVendor = Literal[
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

AI_LINE_SCOPE_INPUT_VENDOR_VALUES: Set[AiLineScopeInputVendor] = {
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


def check_ai_line_scope_input_vendor(value: str) -> AiLineScopeInputVendor:
    if value in AI_LINE_SCOPE_INPUT_VENDOR_VALUES:
        return cast(AiLineScopeInputVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_INPUT_VENDOR_VALUES!r}"
    )
