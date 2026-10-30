from typing import Literal, Set, cast

AiUsageLineVendor = Literal[
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

AI_USAGE_LINE_VENDOR_VALUES: Set[AiUsageLineVendor] = {
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


def check_ai_usage_line_vendor(value: str) -> AiUsageLineVendor:
    if value in AI_USAGE_LINE_VENDOR_VALUES:
        return cast(AiUsageLineVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_USAGE_LINE_VENDOR_VALUES!r}"
    )
