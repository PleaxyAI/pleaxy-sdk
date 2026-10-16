from typing import Literal, Set, cast

ListInvoicesItemBuyerCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_REASON_VALUES: Set[
    ListInvoicesItemBuyerCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_list_invoices_item_buyer_credit_note_reason(
    value: str,
) -> ListInvoicesItemBuyerCreditNoteReason:
    if value in LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_REASON_VALUES:
        return cast(ListInvoicesItemBuyerCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_CREDIT_NOTE_REASON_VALUES!r}"
    )
