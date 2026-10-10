from typing import Literal, Set, cast

RecordPaymentResultUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

RECORD_PAYMENT_RESULT_USAGE_SOURCE_VALUES: Set[RecordPaymentResultUsageSource] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_record_payment_result_usage_source(
    value: str,
) -> RecordPaymentResultUsageSource:
    if value in RECORD_PAYMENT_RESULT_USAGE_SOURCE_VALUES:
        return cast(RecordPaymentResultUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_USAGE_SOURCE_VALUES!r}"
    )
