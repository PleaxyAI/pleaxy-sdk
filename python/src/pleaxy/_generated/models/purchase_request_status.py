from typing import Literal, Set, cast

PurchaseRequestStatus = Literal[
    "approved", "canceled", "draft", "ordered", "pending_approval", "rejected"
]

PURCHASE_REQUEST_STATUS_VALUES: Set[PurchaseRequestStatus] = {
    "approved",
    "canceled",
    "draft",
    "ordered",
    "pending_approval",
    "rejected",
}


def check_purchase_request_status(value: str) -> PurchaseRequestStatus:
    if value in PURCHASE_REQUEST_STATUS_VALUES:
        return cast(PurchaseRequestStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUEST_STATUS_VALUES!r}"
    )
