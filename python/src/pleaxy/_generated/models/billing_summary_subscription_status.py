from typing import Literal, Set, cast

BillingSummarySubscriptionStatus = Literal[
    "active",
    "canceled",
    "incomplete",
    "incomplete_expired",
    "past_due",
    "paused",
    "trialing",
    "unpaid",
]

BILLING_SUMMARY_SUBSCRIPTION_STATUS_VALUES: Set[BillingSummarySubscriptionStatus] = {
    "active",
    "canceled",
    "incomplete",
    "incomplete_expired",
    "past_due",
    "paused",
    "trialing",
    "unpaid",
}


def check_billing_summary_subscription_status(
    value: str,
) -> BillingSummarySubscriptionStatus:
    if value in BILLING_SUMMARY_SUBSCRIPTION_STATUS_VALUES:
        return cast(BillingSummarySubscriptionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BILLING_SUMMARY_SUBSCRIPTION_STATUS_VALUES!r}"
    )
