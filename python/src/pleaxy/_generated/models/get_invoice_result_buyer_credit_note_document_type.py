from typing import Literal, Set, cast

GetInvoiceResultBuyerCreditNoteDocumentType = Literal["credit_note"]

GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    GetInvoiceResultBuyerCreditNoteDocumentType
] = {
    "credit_note",
}


def check_get_invoice_result_buyer_credit_note_document_type(
    value: str,
) -> GetInvoiceResultBuyerCreditNoteDocumentType:
    if value in GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(GetInvoiceResultBuyerCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
