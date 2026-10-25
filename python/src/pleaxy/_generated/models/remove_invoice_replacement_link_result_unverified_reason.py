from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultUnverifiedReason = Literal[
    "debit_note", "no_billing_connection", "no_purchase_order", "payer_account_unclear"
]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_UNVERIFIED_REASON_VALUES: Set[
    RemoveInvoiceReplacementLinkResultUnverifiedReason
] = {
    "debit_note",
    "no_billing_connection",
    "no_purchase_order",
    "payer_account_unclear",
}


def check_remove_invoice_replacement_link_result_unverified_reason(
    value: str,
) -> RemoveInvoiceReplacementLinkResultUnverifiedReason:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_UNVERIFIED_REASON_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_UNVERIFIED_REASON_VALUES!r}"
    )
