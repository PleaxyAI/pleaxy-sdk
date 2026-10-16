from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteSource = Literal["cloud_sync", "feed"]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteSource
] = {
    "cloud_sync",
    "feed",
}


def check_create_invoice_result_supplier_credit_note_source(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteSource:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_SOURCE_VALUES!r}"
    )
