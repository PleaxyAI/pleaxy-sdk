from typing import Literal, Set, cast

AiSavingRecommendationVendor = Literal[
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

AI_SAVING_RECOMMENDATION_VENDOR_VALUES: Set[AiSavingRecommendationVendor] = {
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


def check_ai_saving_recommendation_vendor(value: str) -> AiSavingRecommendationVendor:
    if value in AI_SAVING_RECOMMENDATION_VENDOR_VALUES:
        return cast(AiSavingRecommendationVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SAVING_RECOMMENDATION_VENDOR_VALUES!r}"
    )
