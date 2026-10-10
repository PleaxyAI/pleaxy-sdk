from typing import Literal, Set, cast

SetSupplierCurrenciesResultType0CloudProvider = Literal["aws", "azure", "gcp", "oci"]

SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES: Set[
    SetSupplierCurrenciesResultType0CloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_set_supplier_currencies_result_type_0_cloud_provider(
    value: str,
) -> SetSupplierCurrenciesResultType0CloudProvider:
    if value in SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES:
        return cast(SetSupplierCurrenciesResultType0CloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_SUPPLIER_CURRENCIES_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES!r}"
    )
