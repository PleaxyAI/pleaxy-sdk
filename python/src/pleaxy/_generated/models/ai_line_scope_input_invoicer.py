from typing import Literal, Set, cast

AiLineScopeInputInvoicer = Literal[
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
]

AI_LINE_SCOPE_INPUT_INVOICER_VALUES: Set[AiLineScopeInputInvoicer] = {
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
}


def check_ai_line_scope_input_invoicer(value: str) -> AiLineScopeInputInvoicer:
    if value in AI_LINE_SCOPE_INPUT_INVOICER_VALUES:
        return cast(AiLineScopeInputInvoicer, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_LINE_SCOPE_INPUT_INVOICER_VALUES!r}"
    )
