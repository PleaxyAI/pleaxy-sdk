from typing import Literal, Set, cast

AiProviderProvider = Literal[
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

AI_PROVIDER_PROVIDER_VALUES: Set[AiProviderProvider] = {
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_ai_provider_provider(value: str) -> AiProviderProvider:
    if value in AI_PROVIDER_PROVIDER_VALUES:
        return cast(AiProviderProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_PROVIDER_VALUES!r}"
    )
