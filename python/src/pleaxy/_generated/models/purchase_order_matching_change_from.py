from typing import Literal, Set, cast

PurchaseOrderMatchingChangeFrom = Literal["three_way", "two_way"]

PURCHASE_ORDER_MATCHING_CHANGE_FROM_VALUES: Set[PurchaseOrderMatchingChangeFrom] = {
    "three_way",
    "two_way",
}


def check_purchase_order_matching_change_from(
    value: str,
) -> PurchaseOrderMatchingChangeFrom:
    if value in PURCHASE_ORDER_MATCHING_CHANGE_FROM_VALUES:
        return cast(PurchaseOrderMatchingChangeFrom, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_MATCHING_CHANGE_FROM_VALUES!r}"
    )
