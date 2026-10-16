from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteSubmittedFormat = Literal["cxml", "json", "ubl"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_get_invoice_result_buyer_credit_note_submitted_format(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteSubmittedFormat:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
