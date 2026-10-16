from typing import Literal, Set, cast

ListInvoicesItemSupplierCreditNoteCloudProvider = Literal["aws", "azure", "gcp", "oci"]

LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    ListInvoicesItemSupplierCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_list_invoices_item_supplier_credit_note_cloud_provider(
    value: str,
) -> ListInvoicesItemSupplierCreditNoteCloudProvider:
    if value in LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(ListInvoicesItemSupplierCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_SUPPLIER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
