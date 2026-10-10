from typing import Literal, Set, cast

SetSupplierCurrenciesResultType1CloudProvider = Literal["aws", "azure", "gcp", "oci"]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES: Set[
    SetSupplierCurrenciesResultType1CloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_set_supplier_currencies_result_type_1_cloud_provider(
    value: str,
) -> SetSupplierCurrenciesResultType1CloudProvider:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES:
        return cast(SetSupplierCurrenciesResultType1CloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES!r}"
    )
