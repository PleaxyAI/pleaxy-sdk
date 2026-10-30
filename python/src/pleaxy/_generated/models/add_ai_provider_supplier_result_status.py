from typing import Literal, Set, cast

AddAiProviderSupplierResultStatus = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

ADD_AI_PROVIDER_SUPPLIER_RESULT_STATUS_VALUES: Set[
    AddAiProviderSupplierResultStatus
] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_add_ai_provider_supplier_result_status(
    value: str,
) -> AddAiProviderSupplierResultStatus:
    if value in ADD_AI_PROVIDER_SUPPLIER_RESULT_STATUS_VALUES:
        return cast(AddAiProviderSupplierResultStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_AI_PROVIDER_SUPPLIER_RESULT_STATUS_VALUES!r}"
    )
