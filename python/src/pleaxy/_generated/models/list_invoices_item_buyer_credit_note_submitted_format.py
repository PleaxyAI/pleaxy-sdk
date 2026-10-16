from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteSubmittedFormat = Literal["cxml", "json", "ubl"]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_list_invoices_item_buyer_credit_note_submitted_format(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteSubmittedFormat:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
