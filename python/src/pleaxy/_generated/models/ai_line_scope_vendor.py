from typing import Literal, Set, cast

AiLineScopeVendor = Literal[
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

AI_LINE_SCOPE_VENDOR_VALUES: Set[AiLineScopeVendor] = {
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


def check_ai_line_scope_vendor(value: str) -> AiLineScopeVendor:
    if value in AI_LINE_SCOPE_VENDOR_VALUES:
        return cast(AiLineScopeVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_VENDOR_VALUES!r}"
    )
