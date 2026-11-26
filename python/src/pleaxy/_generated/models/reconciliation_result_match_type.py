from typing import Literal, Set, cast

ReconciliationResultMatchType = Literal["three_way", "two_way", "usage"]

RECONCILIATION_RESULT_MATCH_TYPE_VALUES: Set[ReconciliationResultMatchType] = {
    "three_way",
    "two_way",
    "usage",
}


def check_reconciliation_result_match_type(value: str) -> ReconciliationResultMatchType:
    if value in RECONCILIATION_RESULT_MATCH_TYPE_VALUES:
        return cast(ReconciliationResultMatchType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_MATCH_TYPE_VALUES!r}"
    )
