from typing import Literal, Set, cast

AiCommitmentViewAiVendor = Literal[
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

AI_COMMITMENT_VIEW_AI_VENDOR_VALUES: Set[AiCommitmentViewAiVendor] = {
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


def check_ai_commitment_view_ai_vendor(value: str) -> AiCommitmentViewAiVendor:
    if value in AI_COMMITMENT_VIEW_AI_VENDOR_VALUES:
        return cast(AiCommitmentViewAiVendor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_COMMITMENT_VIEW_AI_VENDOR_VALUES!r}"
    )
