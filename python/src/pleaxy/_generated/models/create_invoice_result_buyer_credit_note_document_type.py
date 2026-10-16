from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteDocumentType = Literal["credit_note"]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteDocumentType
] = {
    "credit_note",
}


def check_create_invoice_result_buyer_credit_note_document_type(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteDocumentType:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_DOCUMENT_TYPE_VALUES!r}"
    )
