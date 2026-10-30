from typing import Literal, Set, cast

AiSpendGroupInvoicer = Literal[
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "gcp",
    "lambda",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

AI_SPEND_GROUP_INVOICER_VALUES: Set[AiSpendGroupInvoicer] = {
    "anthropic",
    "aws",
    "azure",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "gcp",
    "lambda",
    "mistral",
    "nebius",
    "oci",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_ai_spend_group_invoicer(value: str) -> AiSpendGroupInvoicer:
    if value in AI_SPEND_GROUP_INVOICER_VALUES:
        return cast(AiSpendGroupInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_SPEND_GROUP_INVOICER_VALUES!r}"
    )
