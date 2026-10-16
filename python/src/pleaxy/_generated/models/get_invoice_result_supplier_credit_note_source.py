from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteSource = Literal["cloud_sync", "feed"]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_get_invoice_result_supplier_credit_note_source(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteSource:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
