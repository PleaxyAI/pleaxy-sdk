from typing import Literal, Set, cast

PurchaseRequestLineLineType = Literal["goods", "service"]

PURCHASE_REQUEST_LINE_LINE_TYPE_VALUES: Set[PurchaseRequestLineLineType] = {
    "goods",
    "service",
}


def check_purchase_request_line_line_type(value: str) -> PurchaseRequestLineLineType:
    if value in PURCHASE_REQUEST_LINE_LINE_TYPE_VALUES:
        return cast(PurchaseRequestLineLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUEST_LINE_LINE_TYPE_VALUES!r}"
    )
