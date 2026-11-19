from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceCloudProvider = Literal["aws", "azure", "gcp", "oci"]

LIST_INVOICES_ITEM_BUYER_INVOICE_CLOUD_PROVIDER_VALUES: Set[
    ListInvoicesItemBuyerInvoiceCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_list_invoices_item_buyer_invoice_cloud_provider(
    value: str,
) -> ListInvoicesItemBuyerInvoiceCloudProvider:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_CLOUD_PROVIDER_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_CLOUD_PROVIDER_VALUES!r}"
    )
