from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteEnteredBy = Literal["buyer", "supplier"]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_list_invoices_item_buyer_credit_note_entered_by(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteEnteredBy:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES!r}"
    )
