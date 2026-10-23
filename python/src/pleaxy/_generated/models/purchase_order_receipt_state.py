from typing import Literal, Set, cast

PurchaseOrderReceiptState = Literal["full", "none", "partial"]

PURCHASE_ORDER_RECEIPT_STATE_VALUES: Set[PurchaseOrderReceiptState] = {
    "full",
    "none",
    "partial",
}


def check_purchase_order_receipt_state(value: str) -> PurchaseOrderReceiptState:
    if value in PURCHASE_ORDER_RECEIPT_STATE_VALUES:
        return cast(PurchaseOrderReceiptState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_RECEIPT_STATE_VALUES!r}"
    )
