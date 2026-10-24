from typing import Literal, Set, cast

InboundEmailDraftConfirmationLinesItemStatus = Literal[
    "accept", "backordered", "change", "reject"
]

INBOUND_EMAIL_DRAFT_CONFIRMATION_LINES_ITEM_STATUS_VALUES: Set[
    InboundEmailDraftConfirmationLinesItemStatus
] = {
    "accept",
    "backordered",
    "change",
    "reject",
}


def check_inbound_email_draft_confirmation_lines_item_status(
    value: str,
) -> InboundEmailDraftConfirmationLinesItemStatus:
    if value in INBOUND_EMAIL_DRAFT_CONFIRMATION_LINES_ITEM_STATUS_VALUES:
        return cast(InboundEmailDraftConfirmationLinesItemStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DRAFT_CONFIRMATION_LINES_ITEM_STATUS_VALUES!r}"
    )
