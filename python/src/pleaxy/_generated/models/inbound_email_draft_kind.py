from typing import Literal, Set, cast

InboundEmailDraftKind = Literal["confirmation", "shipNotice"]

INBOUND_EMAIL_DRAFT_KIND_VALUES: Set[InboundEmailDraftKind] = {
    "confirmation",
    "shipNotice",
}


def check_inbound_email_draft_kind(value: str) -> InboundEmailDraftKind:
    if value in INBOUND_EMAIL_DRAFT_KIND_VALUES:
        return cast(InboundEmailDraftKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DRAFT_KIND_VALUES!r}"
    )
