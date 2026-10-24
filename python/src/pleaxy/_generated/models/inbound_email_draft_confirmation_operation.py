from typing import Literal, Set, cast

InboundEmailDraftConfirmationOperation = Literal["new", "update"]

INBOUND_EMAIL_DRAFT_CONFIRMATION_OPERATION_VALUES: Set[
    InboundEmailDraftConfirmationOperation
] = {
    "new",
    "update",
}


def check_inbound_email_draft_confirmation_operation(
    value: str,
) -> InboundEmailDraftConfirmationOperation:
    if value in INBOUND_EMAIL_DRAFT_CONFIRMATION_OPERATION_VALUES:
        return cast(InboundEmailDraftConfirmationOperation, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DRAFT_CONFIRMATION_OPERATION_VALUES!r}"
    )
