from typing import Literal, Set, cast

SupplierApprovalViewStatus = Literal["approved", "pending", "rejected"]

SUPPLIER_APPROVAL_VIEW_STATUS_VALUES: Set[SupplierApprovalViewStatus] = {
    "approved",
    "pending",
    "rejected",
}


def check_supplier_approval_view_status(value: str) -> SupplierApprovalViewStatus:
    if value in SUPPLIER_APPROVAL_VIEW_STATUS_VALUES:
        return cast(SupplierApprovalViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_APPROVAL_VIEW_STATUS_VALUES!r}"
    )
