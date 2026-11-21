from typing import Literal, Set, cast

AiProviderProvider = Literal[
    "anthropic",
    "cohere",
    "confluent",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "datadog",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "mongodb",
    "nebius",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "twilio",
    "vercel",
    "xai",
    "zoom",
]

AI_PROVIDER_PROVIDER_VALUES: Set[AiProviderProvider] = {
    "anthropic",
    "cohere",
    "confluent",
    "coreweave",
    "crusoe",
    "cursor",
    "databricks",
    "datadog",
    "github",
    "lambda",
    "microsoft",
    "mistral",
    "mongodb",
    "nebius",
    "openai",
    "openrouter",
    "slack",
    "snowflake",
    "twilio",
    "vercel",
    "xai",
    "zoom",
}


def check_ai_provider_provider(value: str) -> AiProviderProvider:
    if value in AI_PROVIDER_PROVIDER_VALUES:
        return cast(AiProviderProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AI_PROVIDER_PROVIDER_VALUES!r}"
    )
