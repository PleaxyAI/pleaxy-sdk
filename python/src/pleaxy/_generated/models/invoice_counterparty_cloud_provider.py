from typing import Literal, Set, cast

InvoiceCounterpartyCloudProvider = Literal["aws", "azure", "gcp", "oci"]

INVOICE_COUNTERPARTY_CLOUD_PROVIDER_VALUES: Set[InvoiceCounterpartyCloudProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_invoice_counterparty_cloud_provider(
    value: str,
) -> InvoiceCounterpartyCloudProvider:
    if value in INVOICE_COUNTERPARTY_CLOUD_PROVIDER_VALUES:
        return cast(InvoiceCounterpartyCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_COUNTERPARTY_CLOUD_PROVIDER_VALUES!r}"
    )
