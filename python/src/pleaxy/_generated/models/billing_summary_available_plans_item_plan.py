from typing import Literal, Set, cast

BillingSummaryAvailablePlansItemPlan = Literal["autonomous", "managed", "supplier-plus"]

BILLING_SUMMARY_AVAILABLE_PLANS_ITEM_PLAN_VALUES: Set[
    BillingSummaryAvailablePlansItemPlan
] = {
    "autonomous",
    "managed",
    "supplier-plus",
}


def check_billing_summary_available_plans_item_plan(
    value: str,
) -> BillingSummaryAvailablePlansItemPlan:
    if value in BILLING_SUMMARY_AVAILABLE_PLANS_ITEM_PLAN_VALUES:
        return cast(BillingSummaryAvailablePlansItemPlan, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_AVAILABLE_PLANS_ITEM_PLAN_VALUES!r}"
    )
