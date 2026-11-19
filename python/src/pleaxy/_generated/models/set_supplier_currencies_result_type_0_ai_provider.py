from typing import Literal, Set, cast

SetSupplierCurrenciesResultType0AiProvider = Literal[
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_AI_PROVIDER_VALUES: Set[
    SetSupplierCurrenciesResultType0AiProvider
] = {
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
    "slack",
    "snowflake",
    "xai",
    "zoom",
}


def check_set_supplier_currencies_result_type_0_ai_provider(
    value: str,
) -> SetSupplierCurrenciesResultType0AiProvider:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_AI_PROVIDER_VALUES:
        return cast(SetSupplierCurrenciesResultType0AiProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_AI_PROVIDER_VALUES!r}"
    )
