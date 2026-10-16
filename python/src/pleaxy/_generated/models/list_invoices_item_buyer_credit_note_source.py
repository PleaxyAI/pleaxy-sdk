from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteSource = Literal["cloud_sync", "feed"]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SOURCE_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_list_invoices_item_buyer_credit_note_source(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteSource:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
