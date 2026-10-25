from typing import Literal, Set, cast

InvoiceBuyerViewUnverifiedReason = Literal[
    "debit_note", "no_billing_connection", "no_purchase_order", "payer_account_unclear"
]

INVOICE_BUYER_VIEW_UNVERIFIED_REASON_VALUES: Set[InvoiceBuyerViewUnverifiedReason] = {
    "debit_note",
    "no_billing_connection",
    "no_purchase_order",
    "payer_account_unclear",
}


def check_invoice_buyer_view_unverified_reason(
    value: str,
) -> InvoiceBuyerViewUnverifiedReason:
    if value in INVOICE_BUYER_VIEW_UNVERIFIED_REASON_VALUES:
        return cast(InvoiceBuyerViewUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_UNVERIFIED_REASON_VALUES!r}"
    )
