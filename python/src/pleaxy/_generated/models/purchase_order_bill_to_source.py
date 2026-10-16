from typing import Literal, Set, cast

PurchaseOrderBillToSource = Literal["company_profile", "custom"]

PURCHASE_ORDER_BILL_TO_SOURCE_VALUES: Set[PurchaseOrderBillToSource] = {
    "company_profile",
    "custom",
}


def check_purchase_order_bill_to_source(value: str) -> PurchaseOrderBillToSource:
    if value in PURCHASE_ORDER_BILL_TO_SOURCE_VALUES:
        return cast(PurchaseOrderBillToSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_ORDER_BILL_TO_SOURCE_VALUES!r}"
    )
