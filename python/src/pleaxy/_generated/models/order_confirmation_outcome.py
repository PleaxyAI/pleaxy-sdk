from typing import Literal, Set, cast

OrderConfirmationOutcome = Literal["accepted", "backordered", "partial", "rejected"]

ORDER_CONFIRMATION_OUTCOME_VALUES: Set[OrderConfirmationOutcome] = {
    "accepted",
    "backordered",
    "partial",
    "rejected",
}


def check_order_confirmation_outcome(value: str) -> OrderConfirmationOutcome:
    if value in ORDER_CONFIRMATION_OUTCOME_VALUES:
        return cast(OrderConfirmationOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_CONFIRMATION_OUTCOME_VALUES!r}"
    )
