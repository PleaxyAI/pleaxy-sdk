from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteCloudProvider = Literal["aws", "azure", "gcp", "oci"]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteCloudProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_list_invoices_item_buyer_credit_note_cloud_provider(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteCloudProvider:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteCloudProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_CLOUD_PROVIDER_VALUES!r}"
    )
