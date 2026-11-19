from typing import Literal, Set, cast

InvoiceBuyerViewCloudProvider = Literal["aws", "azure", "gcp", "oci"]

INVOICE_BUYER_VIEW_CLOUD_PROVIDER_VALUES: Set[InvoiceBuyerViewCloudProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_invoice_buyer_view_cloud_provider(
    value: str,
) -> InvoiceBuyerViewCloudProvider:
    if value in INVOICE_BUYER_VIEW_CLOUD_PROVIDER_VALUES:
        return cast(InvoiceBuyerViewCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_CLOUD_PROVIDER_VALUES!r}"
    )
