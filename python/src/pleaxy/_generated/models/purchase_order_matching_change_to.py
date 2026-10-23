from typing import Literal, Set, cast

PurchaseOrderMatchingChangeTo = Literal["three_way", "two_way"]

PURCHASE_ORDER_MATCHING_CHANGE_TO_VALUES: Set[PurchaseOrderMatchingChangeTo] = {
    "three_way",
    "two_way",
}


def check_purchase_order_matching_change_to(
    value: str,
) -> PurchaseOrderMatchingChangeTo:
    if value in PURCHASE_ORDER_MATCHING_CHANGE_TO_VALUES:
        return cast(PurchaseOrderMatchingChangeTo, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_MATCHING_CHANGE_TO_VALUES!r}"
    )
