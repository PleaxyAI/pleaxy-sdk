from typing import Literal, Set, cast

RejectInvoiceInputReasonCode = Literal[
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
]

REJECT_INVOICE_INPUT_REASON_CODE_VALUES: Set[RejectInvoiceInputReasonCode] = {
    "amount_incorrect",
    "duplicate",
    "missing_or_wrong_po",
    "not_ordered_or_not_received",
    "other",
    "wrong_billing_entity",
}


def check_reject_invoice_input_reason_code(value: str) -> RejectInvoiceInputReasonCode:
    if value in REJECT_INVOICE_INPUT_REASON_CODE_VALUES:
        return cast(RejectInvoiceInputReasonCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REJECT_INVOICE_INPUT_REASON_CODE_VALUES!r}"
    )
