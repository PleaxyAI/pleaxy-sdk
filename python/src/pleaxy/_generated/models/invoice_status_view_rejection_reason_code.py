from typing import Literal, Set, cast

InvoiceStatusViewRejectionReasonCode = Literal[
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
]

INVOICE_STATUS_VIEW_REJECTION_REASON_CODE_VALUES: Set[
    InvoiceStatusViewRejectionReasonCode
] = {
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
}


def check_invoice_status_view_rejection_reason_code(
    value: str,
) -> InvoiceStatusViewRejectionReasonCode:
    if value in INVOICE_STATUS_VIEW_REJECTION_REASON_CODE_VALUES:
        return cast(InvoiceStatusViewRejectionReasonCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_REJECTION_REASON_CODE_VALUES!r}"
    )
