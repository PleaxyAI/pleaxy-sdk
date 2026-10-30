from typing import Literal, Set, cast

AddAiProviderSupplierResultAiProvider = Literal[
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "lambda",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
]

ADD_AI_PROVIDER_SUPPLIER_RESULT_AI_PROVIDER_VALUES: Set[
    AddAiProviderSupplierResultAiProvider
] = {
    "anthropic",
    "cohere",
    "coreweave",
    "crusoe",
    "databricks",
    "lambda",
    "mistral",
    "nebius",
    "openai",
    "openrouter",
    "snowflake",
    "xai",
}


def check_add_ai_provider_supplier_result_ai_provider(
    value: str,
) -> AddAiProviderSupplierResultAiProvider:
    if value in ADD_AI_PROVIDER_SUPPLIER_RESULT_AI_PROVIDER_VALUES:
        return cast(AddAiProviderSupplierResultAiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_AI_PROVIDER_SUPPLIER_RESULT_AI_PROVIDER_VALUES!r}"
    )
