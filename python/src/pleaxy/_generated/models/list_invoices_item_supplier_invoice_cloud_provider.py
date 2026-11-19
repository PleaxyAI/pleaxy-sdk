from typing import Literal, Set, cast

ListInvoicesItemSupplierInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

LIST_INVOICES_ITEM_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    ListInvoicesItemSupplierInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_list_invoices_item_supplier_invoice_cloud_provider(
    value: str,
) -> ListInvoicesItemSupplierInvoiceCloudProvider:
    if value in LIST_INVOICES_ITEM_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(ListInvoicesItemSupplierInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
