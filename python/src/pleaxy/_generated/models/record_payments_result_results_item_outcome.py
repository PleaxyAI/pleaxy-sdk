from typing import Literal, Set, cast

RecordPaymentsResultResultsItemOutcome = Literal[
    "already_recorded", "recorded", "refused"
]

RECORD_PAYMENTS_RESULT_RESULTS_ITEM_OUTCOME_VALUES: Set[
    RecordPaymentsResultResultsItemOutcome
] = {
    "already_recorded",
    "recorded",
    "refused",
}


def check_record_payments_result_results_item_outcome(
    value: str,
) -> RecordPaymentsResultResultsItemOutcome:
    if value in RECORD_PAYMENTS_RESULT_RESULTS_ITEM_OUTCOME_VALUES:
        return cast(RecordPaymentsResultResultsItemOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENTS_RESULT_RESULTS_ITEM_OUTCOME_VALUES!r}"
    )
