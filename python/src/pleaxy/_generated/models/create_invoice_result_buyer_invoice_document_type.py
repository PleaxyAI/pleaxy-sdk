from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceDocumentType = Literal["debit_note", "invoice"]

CREATE_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_create_invoice_result_buyer_invoice_document_type(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceDocumentType:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
