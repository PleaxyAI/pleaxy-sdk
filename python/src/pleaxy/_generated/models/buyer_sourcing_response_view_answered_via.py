from typing import Literal, Set, cast

BuyerSourcingResponseViewAnsweredVia = Literal["link"]

BUYER_SOURCING_RESPONSE_VIEW_ANSWERED_VIA_VALUES: Set[
    BuyerSourcingResponseViewAnsweredVia
] = {
    "link",
}


def check_buyer_sourcing_response_view_answered_via(
    value: str,
) -> BuyerSourcingResponseViewAnsweredVia:
    if value in BUYER_SOURCING_RESPONSE_VIEW_ANSWERED_VIA_VALUES:
        return cast(BuyerSourcingResponseViewAnsweredVia, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_RESPONSE_VIEW_ANSWERED_VIA_VALUES!r}"
    )
