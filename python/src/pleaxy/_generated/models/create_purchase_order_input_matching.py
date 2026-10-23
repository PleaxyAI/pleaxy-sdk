from typing import Literal, Set, cast

CreatePurchaseOrderInputMatching = Literal["three_way", "two_way"]

CREATE_PURCHASE_ORDER_INPUT_MATCHING_VALUES: Set[CreatePurchaseOrderInputMatching] = {
    "three_way",
    "two_way",
}


def check_create_purchase_order_input_matching(
    value: str,
) -> CreatePurchaseOrderInputMatching:
    if value in CREATE_PURCHASE_ORDER_INPUT_MATCHING_VALUES:
        return cast(CreatePurchaseOrderInputMatching, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PURCHASE_ORDER_INPUT_MATCHING_VALUES!r}"
    )
