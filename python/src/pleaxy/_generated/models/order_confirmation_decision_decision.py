from typing import Literal, Set, cast

OrderConfirmationDecisionDecision = Literal["applied", "declined"]

ORDER_CONFIRMATION_DECISION_DECISION_VALUES: Set[OrderConfirmationDecisionDecision] = {
    "applied",
    "declined",
}


def check_order_confirmation_decision_decision(
    value: str,
) -> OrderConfirmationDecisionDecision:
    if value in ORDER_CONFIRMATION_DECISION_DECISION_VALUES:
        return cast(OrderConfirmationDecisionDecision, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_DECISION_DECISION_VALUES!r}"
    )
