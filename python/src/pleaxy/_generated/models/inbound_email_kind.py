from typing import Literal, Set, cast

InboundEmailKind = Literal["cxml", "text"]

INBOUND_EMAIL_KIND_VALUES: Set[InboundEmailKind] = {
    "cxml",
    "text",
}


def check_inbound_email_kind(value: str) -> InboundEmailKind:
    if value in INBOUND_EMAIL_KIND_VALUES:
        return cast(InboundEmailKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_KIND_VALUES!r}"
    )
