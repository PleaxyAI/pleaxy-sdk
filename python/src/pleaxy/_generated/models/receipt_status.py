from typing import Literal, Set, cast

ReceiptStatus = Literal["approved", "pending_approval", "rejected", "reversed"]

RECEIPT_STATUS_VALUES: Set[ReceiptStatus] = {
    "approved",
    "pending_approval",
    "rejected",
    "reversed",
}


def check_receipt_status(value: str) -> ReceiptStatus:
    if value in RECEIPT_STATUS_VALUES:
        return cast(ReceiptStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECEIPT_STATUS_VALUES!r}"
    )
