from typing import Literal, Set, cast

BillingSummaryManagedBy = Literal["platform", "self-serve"]

BILLING_SUMMARY_MANAGED_BY_VALUES: Set[BillingSummaryManagedBy] = {
    "platform",
    "self-serve",
}


def check_billing_summary_managed_by(value: str) -> BillingSummaryManagedBy:
    if value in BILLING_SUMMARY_MANAGED_BY_VALUES:
        return cast(BillingSummaryManagedBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_MANAGED_BY_VALUES!r}"
    )
