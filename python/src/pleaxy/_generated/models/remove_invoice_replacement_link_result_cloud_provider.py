from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultCloudProvider = Literal["aws", "azure", "gcp", "oci"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_CLOUD_PROVIDER_VALUES: Set[
    RemoveInvoiceReplacementLinkResultCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_remove_invoice_replacement_link_result_cloud_provider(
    value: str,
) -> RemoveInvoiceReplacementLinkResultCloudProvider:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_CLOUD_PROVIDER_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_CLOUD_PROVIDER_VALUES!r}"
    )
