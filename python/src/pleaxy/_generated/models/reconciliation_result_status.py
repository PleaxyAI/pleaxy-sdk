from typing import Literal, Set, cast

ReconciliationResultStatus = Literal["disputed", "matched", "pending", "unverified"]

RECONCILIATION_RESULT_STATUS_VALUES: Set[ReconciliationResultStatus] = {
    "disputed",
    "matched",
    "pending",
    "unverified",
}


def check_reconciliation_result_status(value: str) -> ReconciliationResultStatus:
    if value in RECONCILIATION_RESULT_STATUS_VALUES:
        return cast(ReconciliationResultStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_STATUS_VALUES!r}"
    )
