from typing import Literal, Set, cast

ReconciliationResultCheckedItemResult = Literal[
    "fail", "no_failures_recorded", "not_checked", "pass", "pending", "skipped"
]

RECONCILIATION_RESULT_CHECKED_ITEM_RESULT_VALUES: Set[
    ReconciliationResultCheckedItemResult
] = {
    "fail",
    "no_failures_recorded",
    "not_checked",
    "pass",
    "pending",
    "skipped",
}


def check_reconciliation_result_checked_item_result(
    value: str,
) -> ReconciliationResultCheckedItemResult:
    if value in RECONCILIATION_RESULT_CHECKED_ITEM_RESULT_VALUES:
        return cast(ReconciliationResultCheckedItemResult, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_CHECKED_ITEM_RESULT_VALUES!r}"
    )
