from typing import Literal, Set, cast

AddCloudProviderAsSupplierResultAiProvider = Literal[
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

ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_AI_PROVIDER_VALUES: Set[
    AddCloudProviderAsSupplierResultAiProvider
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


def check_add_cloud_provider_as_supplier_result_ai_provider(
    value: str,
) -> AddCloudProviderAsSupplierResultAiProvider:
    if value in ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_AI_PROVIDER_VALUES:
        return cast(AddCloudProviderAsSupplierResultAiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_AI_PROVIDER_VALUES!r}"
    )
