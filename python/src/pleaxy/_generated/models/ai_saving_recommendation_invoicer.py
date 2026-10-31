from typing import Literal, Set, cast

AiSavingRecommendationInvoicer = Literal[
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
    "snowflake",
    "xai",
]

AI_SAVING_RECOMMENDATION_INVOICER_VALUES: Set[AiSavingRecommendationInvoicer] = {
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
    "snowflake",
    "xai",
}


def check_ai_saving_recommendation_invoicer(
    value: str,
) -> AiSavingRecommendationInvoicer:
    if value in AI_SAVING_RECOMMENDATION_INVOICER_VALUES:
        return cast(AiSavingRecommendationInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SAVING_RECOMMENDATION_INVOICER_VALUES!r}"
    )
