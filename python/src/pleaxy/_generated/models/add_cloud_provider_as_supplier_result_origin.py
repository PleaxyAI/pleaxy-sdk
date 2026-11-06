from typing import Literal, Set, cast

AddCloudProviderAsSupplierResultOrigin = Literal["rfq"]

ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_ORIGIN_VALUES: Set[
    AddCloudProviderAsSupplierResultOrigin
] = {
    "rfq",
}


def check_add_cloud_provider_as_supplier_result_origin(
    value: str,
) -> AddCloudProviderAsSupplierResultOrigin:
    if value in ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_ORIGIN_VALUES:
        return cast(AddCloudProviderAsSupplierResultOrigin, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_ORIGIN_VALUES!r}"
    )
