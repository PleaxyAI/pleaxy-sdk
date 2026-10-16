from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteEnteredBy = Literal["buyer", "supplier"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_get_invoice_result_buyer_credit_note_entered_by(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteEnteredBy:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_ENTERED_BY_VALUES!r}"
    )
