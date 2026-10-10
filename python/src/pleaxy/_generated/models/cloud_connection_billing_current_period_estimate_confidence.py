from typing import Literal, Set, cast

CloudConnectionBillingCurrentPeriodEstimateConfidence = Literal["estimate_in_progress"]

CLOUD_CONNECTION_BILLING_CURRENT_PERIOD_ESTIMATE_CONFIDENCE_VALUES: Set[
    CloudConnectionBillingCurrentPeriodEstimateConfidence
] = {
    "estimate_in_progress",
}


def check_cloud_connection_billing_current_period_estimate_confidence(
    value: str,
) -> CloudConnectionBillingCurrentPeriodEstimateConfidence:
    if value in CLOUD_CONNECTION_BILLING_CURRENT_PERIOD_ESTIMATE_CONFIDENCE_VALUES:
        return cast(CloudConnectionBillingCurrentPeriodEstimateConfidence, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_BILLING_CURRENT_PERIOD_ESTIMATE_CONFIDENCE_VALUES!r}"
    )
