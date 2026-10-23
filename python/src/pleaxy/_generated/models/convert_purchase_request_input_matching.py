from typing import Literal, Set, cast

ConvertPurchaseRequestInputMatching = Literal["three_way", "two_way"]

CONVERT_PURCHASE_REQUEST_INPUT_MATCHING_VALUES: Set[
    ConvertPurchaseRequestInputMatching
] = {
    "three_way",
    "two_way",
}


def check_convert_purchase_request_input_matching(
    value: str,
) -> ConvertPurchaseRequestInputMatching:
    if value in CONVERT_PURCHASE_REQUEST_INPUT_MATCHING_VALUES:
        return cast(ConvertPurchaseRequestInputMatching, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERT_PURCHASE_REQUEST_INPUT_MATCHING_VALUES!r}"
    )
