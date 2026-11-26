from typing import Literal, Set, cast

CreateInvoiceResultBuyerCreditNoteSubmittedFormat = Literal[
    "cii", "cxml", "facturae", "fatturapa", "json", "nfe", "nfse", "ubl"
]

CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    CreateInvoiceResultBuyerCreditNoteSubmittedFormat
] = {
    "cii",
    "cxml",
    "facturae",
    "fatturapa",
    "json",
    "nfe",
    "nfse",
    "ubl",
}


def check_create_invoice_result_buyer_credit_note_submitted_format(
    value: str,
) -> CreateInvoiceResultBuyerCreditNoteSubmittedFormat:
    if value in CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(CreateInvoiceResultBuyerCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
