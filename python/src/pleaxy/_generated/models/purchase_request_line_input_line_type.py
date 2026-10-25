from typing import Literal, Set, cast

PurchaseRequestLineInputLineType = Literal["goods", "service"]

PURCHASE_REQUEST_LINE_INPUT_LINE_TYPE_VALUES: Set[PurchaseRequestLineInputLineType] = {
    "goods",
    "service",
}


def check_purchase_request_line_input_line_type(
    value: str,
) -> PurchaseRequestLineInputLineType:
    if value in PURCHASE_REQUEST_LINE_INPUT_LINE_TYPE_VALUES:
        return cast(PurchaseRequestLineInputLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PURCHASE_REQUEST_LINE_INPUT_LINE_TYPE_VALUES!r}"
    )
