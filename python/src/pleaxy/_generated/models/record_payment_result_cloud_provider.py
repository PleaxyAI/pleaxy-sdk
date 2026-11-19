from typing import Literal, Set, cast

RecordPaymentResultCloudProvider = Literal["aws", "azure", "gcp", "oci"]

RECORD_PAYMENT_RESULT_CLOUD_PROVIDER_VALUES: Set[RecordPaymentResultCloudProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_record_payment_result_cloud_provider(
    value: str,
) -> RecordPaymentResultCloudProvider:
    if value in RECORD_PAYMENT_RESULT_CLOUD_PROVIDER_VALUES:
        return cast(RecordPaymentResultCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_CLOUD_PROVIDER_VALUES!r}"
    )
