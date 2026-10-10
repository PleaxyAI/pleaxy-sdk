from typing import Literal, Set, cast

BillingSummaryPlan = Literal[
    "assisted",
    "autonomous",
    "enterprise",
    "managed",
    "supplier-enterprise",
    "supplier-free",
    "supplier-plus",
]

BILLING_SUMMARY_PLAN_VALUES: Set[BillingSummaryPlan] = {
    "assisted",
    "autonomous",
    "enterprise",
    "managed",
    "supplier-enterprise",
    "supplier-free",
    "supplier-plus",
}


def check_billing_summary_plan(value: str) -> BillingSummaryPlan:
    if value in BILLING_SUMMARY_PLAN_VALUES:
        return cast(BillingSummaryPlan, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_PLAN_VALUES!r}"
    )
