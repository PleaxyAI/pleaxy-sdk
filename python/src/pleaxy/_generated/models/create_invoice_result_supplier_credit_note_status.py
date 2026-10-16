from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteStatus = Literal[
    "accepted", "pending_acceptance", "rejected", "void"
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteStatus
] = {
    "accepted",
    "pending_acceptance",
    "rejected",
    "void",
}


def check_create_invoice_result_supplier_credit_note_status(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteStatus:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_STATUS_VALUES!r}"
    )
