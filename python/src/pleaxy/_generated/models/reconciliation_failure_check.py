from typing import Literal, Set, cast

ReconciliationFailureCheck = Literal[
    "agreement_active",
    "agreement_cap",
    "agreement_discount",
    "agreement_rate",
    "commitment_shortfall",
    "milestone_already_billed",
    "milestone_amount",
    "milestone_confirmed",
    "milestone_exists",
    "order_amount",
    "order_line_exists",
    "order_price",
    "order_quantity",
    "receipt_amount",
    "receipt_exists",
    "receipt_quantity",
    "usage_currency",
    "usage_match",
]

RECONCILIATION_FAILURE_CHECK_VALUES: Set[ReconciliationFailureCheck] = {
    "agreement_active",
    "agreement_cap",
    "agreement_discount",
    "agreement_rate",
    "commitment_shortfall",
    "milestone_already_billed",
    "milestone_amount",
    "milestone_confirmed",
    "milestone_exists",
    "order_amount",
    "order_line_exists",
    "order_price",
    "order_quantity",
    "receipt_amount",
    "receipt_exists",
    "receipt_quantity",
    "usage_currency",
    "usage_match",
}


def check_reconciliation_failure_check(value: str) -> ReconciliationFailureCheck:
    if value in RECONCILIATION_FAILURE_CHECK_VALUES:
        return cast(ReconciliationFailureCheck, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_FAILURE_CHECK_VALUES!r}"
    )
