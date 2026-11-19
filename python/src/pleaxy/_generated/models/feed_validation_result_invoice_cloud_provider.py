from typing import Literal, Set, cast

FeedValidationResultInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

FEED_VALIDATION_RESULT_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    FeedValidationResultInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_feed_validation_result_invoice_cloud_provider(
    value: str,
) -> FeedValidationResultInvoiceCloudProvider:
    if value in FEED_VALIDATION_RESULT_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(FeedValidationResultInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEED_VALIDATION_RESULT_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
