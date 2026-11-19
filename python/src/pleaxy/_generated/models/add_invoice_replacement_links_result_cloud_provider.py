from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultCloudProvider = Literal["aws", "azure", "gcp", "oci"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_CLOUD_PROVIDER_VALUES: Set[
    AddInvoiceReplacementLinksResultCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_add_invoice_replacement_links_result_cloud_provider(
    value: str,
) -> AddInvoiceReplacementLinksResultCloudProvider:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_CLOUD_PROVIDER_VALUES:
        return cast(AddInvoiceReplacementLinksResultCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_CLOUD_PROVIDER_VALUES!r}"
    )
