from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_get_invoice_result_supplier_credit_note_status(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteStatus:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
