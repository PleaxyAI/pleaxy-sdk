from typing import Literal, Set, cast

SetInvoiceFeedResultType0CloudProvider = Literal["aws", "azure", "gcp", "oci"]

SET_INVOICE_FEED_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES: Set[
    SetInvoiceFeedResultType0CloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_set_invoice_feed_result_type_0_cloud_provider(
    value: str,
) -> SetInvoiceFeedResultType0CloudProvider:
    if value in SET_INVOICE_FEED_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES:
        return cast(SetInvoiceFeedResultType0CloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_INVOICE_FEED_RESULT_TYPE_0_CLOUD_PROVIDER_VALUES!r}"
    )
