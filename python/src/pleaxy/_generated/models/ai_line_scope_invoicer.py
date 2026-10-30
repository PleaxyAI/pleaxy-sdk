from typing import Literal, Set, cast

AiLineScopeInvoicer = Literal[
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

AI_LINE_SCOPE_INVOICER_VALUES: Set[AiLineScopeInvoicer] = {
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


def check_ai_line_scope_invoicer(value: str) -> AiLineScopeInvoicer:
    if value in AI_LINE_SCOPE_INVOICER_VALUES:
        return cast(AiLineScopeInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_INVOICER_VALUES!r}"
    )
