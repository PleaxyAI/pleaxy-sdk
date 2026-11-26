from typing import Literal, Set, cast

ReconciliationResultPrimaryFailure = Literal[
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

RECONCILIATION_RESULT_PRIMARY_FAILURE_VALUES: Set[
    ReconciliationResultPrimaryFailure
] = {
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


def check_reconciliation_result_primary_failure(
    value: str,
) -> ReconciliationResultPrimaryFailure:
    if value in RECONCILIATION_RESULT_PRIMARY_FAILURE_VALUES:
        return cast(ReconciliationResultPrimaryFailure, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_PRIMARY_FAILURE_VALUES!r}"
    )
