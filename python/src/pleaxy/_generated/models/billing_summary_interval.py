from typing import Literal, Set, cast

BillingSummaryInterval = Literal["month", "year"]

BILLING_SUMMARY_INTERVAL_VALUES: Set[BillingSummaryInterval] = {
    "month",
    "year",
}


def check_billing_summary_interval(value: str) -> BillingSummaryInterval:
    if value in BILLING_SUMMARY_INTERVAL_VALUES:
        return cast(BillingSummaryInterval, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_INTERVAL_VALUES!r}"
    )
