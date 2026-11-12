from typing import Literal, Set, cast

BuyerSourcingInviteeViewState = Literal["declined", "invited", "responded", "viewed"]

BUYER_SOURCING_INVITEE_VIEW_STATE_VALUES: Set[BuyerSourcingInviteeViewState] = {
    "declined",
    "invited",
    "responded",
    "viewed",
}


def check_buyer_sourcing_invitee_view_state(
    value: str,
) -> BuyerSourcingInviteeViewState:
    if value in BUYER_SOURCING_INVITEE_VIEW_STATE_VALUES:
        return cast(BuyerSourcingInviteeViewState, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUYER_SOURCING_INVITEE_VIEW_STATE_VALUES!r}"
    )
