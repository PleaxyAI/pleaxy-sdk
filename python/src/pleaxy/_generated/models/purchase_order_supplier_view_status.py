from typing import Literal, Set, cast

PurchaseOrderSupplierViewStatus = Literal[
    "awaiting_fulfillment",
    "canceled",
    "closed",
    "draft",
    "expired",
    "invoiced",
    "paid",
    "pending_approval",
    "rejected",
]

PURCHASE_ORDER_SUPPLIER_VIEW_STATUS_VALUES: Set[PurchaseOrderSupplierViewStatus] = {
    "awaiting_fulfillment",
    "canceled",
    "closed",
    "draft",
    "expired",
    "invoiced",
    "paid",
    "pending_approval",
    "rejected",
}


def check_purchase_order_supplier_view_status(
    value: str,
) -> PurchaseOrderSupplierViewStatus:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_STATUS_VALUES:
        return cast(PurchaseOrderSupplierViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_STATUS_VALUES!r}"
    )
