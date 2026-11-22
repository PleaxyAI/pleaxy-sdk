from typing import Literal, Set, cast

CreateInvoiceResultSupplierCreditNoteReason = Literal[
    "early_payment_discount",
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
]

CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES: Set[
    CreateInvoiceResultSupplierCreditNoteReason
] = {
    "early_payment_discount",
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_create_invoice_result_supplier_credit_note_reason(
    value: str,
) -> CreateInvoiceResultSupplierCreditNoteReason:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES:
        return cast(CreateInvoiceResultSupplierCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES!r}"
    )
