from typing import Literal, Set, cast

AiRateCardEntryVendor = Literal[
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

AI_RATE_CARD_ENTRY_VENDOR_VALUES: Set[AiRateCardEntryVendor] = {
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


def check_ai_rate_card_entry_vendor(value: str) -> AiRateCardEntryVendor:
    if value in AI_RATE_CARD_ENTRY_VENDOR_VALUES:
        return cast(AiRateCardEntryVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_RATE_CARD_ENTRY_VENDOR_VALUES!r}"
    )
