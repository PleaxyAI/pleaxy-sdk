from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteSubmittedFormat = Literal[
    "cii", "cxml", "facturae", "fatturapa", "json", "nfe", "nfse", "ubl"
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteSubmittedFormat
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


def check_create_invoice_result_supplier_credit_note_submitted_format(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteSubmittedFormat:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SUBMITTED_FORMAT_VALUES!r}"
    )
