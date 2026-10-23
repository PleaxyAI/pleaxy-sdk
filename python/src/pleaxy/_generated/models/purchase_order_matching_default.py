from typing import Literal, Set, cast

PurchaseOrderMatchingDefault = Literal["three_way", "two_way"]

PURCHASE_ORDER_MATCHING_DEFAULT_VALUES: Set[PurchaseOrderMatchingDefault] = {
    "three_way",
    "two_way",
}


def check_purchase_order_matching_default(value: str) -> PurchaseOrderMatchingDefault:
    if value in PURCHASE_ORDER_MATCHING_DEFAULT_VALUES:
        return cast(PurchaseOrderMatchingDefault, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_MATCHING_DEFAULT_VALUES!r}"
    )
