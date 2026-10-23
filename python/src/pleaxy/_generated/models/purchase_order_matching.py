from typing import Literal, Set, cast

PurchaseOrderMatching = Literal["three_way", "two_way"]

PURCHASE_ORDER_MATCHING_VALUES: Set[PurchaseOrderMatching] = {
    "three_way",
    "two_way",
}


def check_purchase_order_matching(value: str) -> PurchaseOrderMatching:
    if value in PURCHASE_ORDER_MATCHING_VALUES:
        return cast(PurchaseOrderMatching, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_MATCHING_VALUES!r}"
    )
