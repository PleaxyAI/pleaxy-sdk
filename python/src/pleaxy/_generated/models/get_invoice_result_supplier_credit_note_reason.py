from typing import Literal, Set, cast

GetInvoiceResultSupplierCreditNoteReason = Literal[
    "other", "price_adjustment", "rebate", "returned_goods", "service_credit"
]

GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES: Set[
    GetInvoiceResultSupplierCreditNoteReason
] = {
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_get_invoice_result_supplier_credit_note_reason(
    value: str,
) -> GetInvoiceResultSupplierCreditNoteReason:
    if value in GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES:
        return cast(GetInvoiceResultSupplierCreditNoteReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_CREDIT_NOTE_REASON_VALUES!r}"
    )
