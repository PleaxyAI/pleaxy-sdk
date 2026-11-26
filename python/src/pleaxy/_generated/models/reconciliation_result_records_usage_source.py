from typing import Literal, Set, cast

ReconciliationResultRecordsUsageSource = Literal["provider_invoice", "provider_report"]

RECONCILIATION_RESULT_RECORDS_USAGE_SOURCE_VALUES: Set[
    ReconciliationResultRecordsUsageSource
] = {
    "provider_invoice",
    "provider_report",
}


def check_reconciliation_result_records_usage_source(
    value: str,
) -> ReconciliationResultRecordsUsageSource:
    if value in RECONCILIATION_RESULT_RECORDS_USAGE_SOURCE_VALUES:
        return cast(ReconciliationResultRecordsUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECONCILIATION_RESULT_RECORDS_USAGE_SOURCE_VALUES!r}"
    )
