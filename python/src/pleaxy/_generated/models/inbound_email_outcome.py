from typing import Literal, Set, cast

InboundEmailOutcome = Literal[
    "applied", "draft", "failed", "held", "ignored", "noAction", "test"
]

INBOUND_EMAIL_OUTCOME_VALUES: Set[InboundEmailOutcome] = {
    "applied",
    "draft",
    "failed",
    "held",
    "ignored",
    "noAction",
    "test",
}


def check_inbound_email_outcome(value: str) -> InboundEmailOutcome:
    if value in INBOUND_EMAIL_OUTCOME_VALUES:
        return cast(InboundEmailOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_OUTCOME_VALUES!r}"
    )
