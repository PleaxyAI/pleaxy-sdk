from typing import Literal, Set, cast

InvoiceRejectionReasonCode = Literal[
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
]

INVOICE_REJECTION_REASON_CODE_VALUES: Set[InvoiceRejectionReasonCode] = {
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
}


def check_invoice_rejection_reason_code(value: str) -> InvoiceRejectionReasonCode:
    if value in INVOICE_REJECTION_REASON_CODE_VALUES:
        return cast(InvoiceRejectionReasonCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_REJECTION_REASON_CODE_VALUES!r}"
    )
