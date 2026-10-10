from typing import Literal, Set, cast

AddCloudProviderAsSupplierResultCloudProvider = Literal["aws", "azure", "gcp", "oci"]

ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES: Set[
    AddCloudProviderAsSupplierResultCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_add_cloud_provider_as_supplier_result_cloud_provider(
    value: str,
) -> AddCloudProviderAsSupplierResultCloudProvider:
    if value in ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES:
        return cast(AddCloudProviderAsSupplierResultCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES!r}"
    )
