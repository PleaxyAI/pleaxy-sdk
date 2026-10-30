from typing import Literal, Set, cast

AddAiProviderSupplierResultCloudProvider = Literal["aws", "azure", "gcp", "oci"]

ADD_AI_PROVIDER_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES: Set[
    AddAiProviderSupplierResultCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_add_ai_provider_supplier_result_cloud_provider(
    value: str,
) -> AddAiProviderSupplierResultCloudProvider:
    if value in ADD_AI_PROVIDER_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES:
        return cast(AddAiProviderSupplierResultCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_AI_PROVIDER_SUPPLIER_RESULT_CLOUD_PROVIDER_VALUES!r}"
    )
