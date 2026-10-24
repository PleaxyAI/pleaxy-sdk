from typing import Literal, Set, cast

InboundEmailTrust = Literal["unverified", "verified"]

INBOUND_EMAIL_TRUST_VALUES: Set[InboundEmailTrust] = {
    "unverified",
    "verified",
}


def check_inbound_email_trust(value: str) -> InboundEmailTrust:
    if value in INBOUND_EMAIL_TRUST_VALUES:
        return cast(InboundEmailTrust, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_TRUST_VALUES!r}"
    )
