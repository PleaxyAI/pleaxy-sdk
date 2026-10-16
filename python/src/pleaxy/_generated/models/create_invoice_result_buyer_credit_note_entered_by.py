from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteEnteredBy = Literal["buyer", "supplier"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_create_invoice_result_buyer_credit_note_entered_by(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteEnteredBy:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES!r}"
    )
