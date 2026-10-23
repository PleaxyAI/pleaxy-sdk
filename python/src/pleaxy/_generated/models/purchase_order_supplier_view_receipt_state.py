from typing import Literal, Set, cast

PurchaseOrderSupplierViewReceiptState = Literal["full", "none", "partial"]

PURCHASE_ORDER_SUPPLIER_VIEW_RECEIPT_STATE_VALUES: Set[
    PurchaseOrderSupplierViewReceiptState
] = {
    "full",
    "none",
    "partial",
}


def check_purchase_order_supplier_view_receipt_state(
    value: str,
) -> PurchaseOrderSupplierViewReceiptState:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_RECEIPT_STATE_VALUES:
        return cast(PurchaseOrderSupplierViewReceiptState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_RECEIPT_STATE_VALUES!r}"
    )
