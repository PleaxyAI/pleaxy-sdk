from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_get_invoice_result_buyer_credit_note_status(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteStatus:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
