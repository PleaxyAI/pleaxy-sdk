from typing import Literal, Set, cast

SetInvoiceFeedResultType1CloudProvider = Literal["aws", "azure", "gcp", "oci"]

SET_INVOICE_FEED_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES: Set[
    SetInvoiceFeedResultType1CloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_set_invoice_feed_result_type_1_cloud_provider(
    value: str,
) -> SetInvoiceFeedResultType1CloudProvider:
    if value in SET_INVOICE_FEED_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES:
        return cast(SetInvoiceFeedResultType1CloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_1_CLOUD_PROVIDER_VALUES!r}"
    )
