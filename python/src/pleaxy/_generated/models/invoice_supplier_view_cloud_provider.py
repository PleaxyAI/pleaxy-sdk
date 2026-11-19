from typing import Literal, Set, cast

InvoiceSupplierViewCloudProvider = Literal["aws", "azure", "gcp", "oci"]

INVOICE_SUPPLIER_VIEW_CLOUD_PROVIDER_VALUES: Set[InvoiceSupplierViewCloudProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_invoice_supplier_view_cloud_provider(
    value: str,
) -> InvoiceSupplierViewCloudProvider:
    if value in INVOICE_SUPPLIER_VIEW_CLOUD_PROVIDER_VALUES:
        return cast(InvoiceSupplierViewCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_CLOUD_PROVIDER_VALUES!r}"
    )
