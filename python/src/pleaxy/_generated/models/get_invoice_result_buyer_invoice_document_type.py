from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceDocumentType = Literal["debit_note", "invoice"]

GET_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES: Set[
    GetInvoiceResultBuyerInvoiceDocumentType
] = {
    "debit_note",
    "invoice",
}


def check_get_invoice_result_buyer_invoice_document_type(
    value: str,
) -> GetInvoiceResultBuyerInvoiceDocumentType:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_DOCUMENT_TYPE_VALUES!r}"
    )
