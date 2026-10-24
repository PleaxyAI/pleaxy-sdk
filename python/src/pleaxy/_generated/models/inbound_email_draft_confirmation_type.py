from typing import Literal, Set, cast

InboundEmailDraftConfirmationType = Literal["accept", "backordered", "detail", "reject"]

INBOUND_EMAIL_DRAFT_CONFIRMATION_TYPE_VALUES: Set[InboundEmailDraftConfirmationType] = {
    "accept",
    "backordered",
    "detail",
    "reject",
}


def check_inbound_email_draft_confirmation_type(
    value: str,
) -> InboundEmailDraftConfirmationType:
    if value in INBOUND_EMAIL_DRAFT_CONFIRMATION_TYPE_VALUES:
        return cast(InboundEmailDraftConfirmationType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DRAFT_CONFIRMATION_TYPE_VALUES!r}"
    )
