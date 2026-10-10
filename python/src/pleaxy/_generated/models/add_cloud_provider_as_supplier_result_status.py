from typing import Literal, Set, cast

AddCloudProviderAsSupplierResultStatus = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_STATUS_VALUES: Set[
    AddCloudProviderAsSupplierResultStatus
] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_add_cloud_provider_as_supplier_result_status(
    value: str,
) -> AddCloudProviderAsSupplierResultStatus:
    if value in ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_STATUS_VALUES:
        return cast(AddCloudProviderAsSupplierResultStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_CLOUD_PROVIDER_AS_SUPPLIER_RESULT_STATUS_VALUES!r}"
    )
