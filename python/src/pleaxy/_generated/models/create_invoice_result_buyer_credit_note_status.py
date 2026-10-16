from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_create_invoice_result_buyer_credit_note_status(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteStatus:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
