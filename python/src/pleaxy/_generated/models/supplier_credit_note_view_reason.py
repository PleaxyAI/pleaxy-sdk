from typing import Literal, Set, cast

SupplierCreditNoteViewReason = Literal[
    "early_payment_discount",
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
]

SUPPLIER_CREDIT_NOTE_VIEW_REASON_VALUES: Set[SupplierCreditNoteViewReason] = {
    "early_payment_discount",
    "other",
    "price_adjustment",
    "rebate",
    "returned_goods",
    "service_credit",
}


def check_supplier_credit_note_view_reason(value: str) -> SupplierCreditNoteViewReason:
    if value in SUPPLIER_CREDIT_NOTE_VIEW_REASON_VALUES:
        return cast(SupplierCreditNoteViewReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SUPPLIER_CREDIT_NOTE_VIEW_REASON_VALUES!r}"
    )
