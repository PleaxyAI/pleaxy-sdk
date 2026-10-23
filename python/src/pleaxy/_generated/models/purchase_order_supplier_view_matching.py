from typing import Literal, Set, cast

PurchaseOrderSupplierViewMatching = Literal["three_way", "two_way"]

PURCHASE_ORDER_SUPPLIER_VIEW_MATCHING_VALUES: Set[PurchaseOrderSupplierViewMatching] = {
    "three_way",
    "two_way",
}


def check_purchase_order_supplier_view_matching(
    value: str,
) -> PurchaseOrderSupplierViewMatching:
    if value in PURCHASE_ORDER_SUPPLIER_VIEW_MATCHING_VALUES:
        return cast(PurchaseOrderSupplierViewMatching, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_SUPPLIER_VIEW_MATCHING_VALUES!r}"
    )
