from typing import Literal, Set, cast

ListPurchaseRequestsStatus = Literal[
    "approved", "canceled", "draft", "ordered", "pending_approval", "rejected"
]

LIST_PURCHASE_REQUESTS_STATUS_VALUES: Set[ListPurchaseRequestsStatus] = {
    "approved",
    "canceled",
    "draft",
    "ordered",
    "pending_approval",
    "rejected",
}


def check_list_purchase_requests_status(value: str) -> ListPurchaseRequestsStatus:
    if value in LIST_PURCHASE_REQUESTS_STATUS_VALUES:
        return cast(ListPurchaseRequestsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PURCHASE_REQUESTS_STATUS_VALUES!r}"
    )
