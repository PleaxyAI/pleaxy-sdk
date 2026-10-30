from typing import Literal, Set, cast

AiCommitmentViewAiInvoicer = Literal[
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

AI_COMMITMENT_VIEW_AI_INVOICER_VALUES: Set[AiCommitmentViewAiInvoicer] = {
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


def check_ai_commitment_view_ai_invoicer(value: str) -> AiCommitmentViewAiInvoicer:
    if value in AI_COMMITMENT_VIEW_AI_INVOICER_VALUES:
        return cast(AiCommitmentViewAiInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_COMMITMENT_VIEW_AI_INVOICER_VALUES!r}"
    )
