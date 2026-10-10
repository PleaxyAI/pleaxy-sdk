from typing import Literal, Set, cast

PurchaseOrderSupplierInviteStatus = Literal[
    "existing", "failed", "invited", "needs_permission"
]

PURCHASE_ORDER_SUPPLIER_INVITE_STATUS_VALUES: Set[PurchaseOrderSupplierInviteStatus] = {
    "existing",
    "failed",
    "invited",
    "needs_permission",
}


def check_purchase_order_supplier_invite_status(
    value: str,
) -> PurchaseOrderSupplierInviteStatus:
    if value in PURCHASE_ORDER_SUPPLIER_INVITE_STATUS_VALUES:
        return cast(PurchaseOrderSupplierInviteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_INVITE_STATUS_VALUES!r}"
    )
