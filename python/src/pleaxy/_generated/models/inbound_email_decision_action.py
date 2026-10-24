from typing import Literal, Set, cast

InboundEmailDecisionAction = Literal["dismissed", "recorded"]

INBOUND_EMAIL_DECISION_ACTION_VALUES: Set[InboundEmailDecisionAction] = {
    "dismissed",
    "recorded",
}


def check_inbound_email_decision_action(value: str) -> InboundEmailDecisionAction:
    if value in INBOUND_EMAIL_DECISION_ACTION_VALUES:
        return cast(InboundEmailDecisionAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOUND_EMAIL_DECISION_ACTION_VALUES!r}"
    )
