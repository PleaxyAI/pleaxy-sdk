from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceUnverifiedReason = Literal[
    "debit_note",
    "no_billing_connection",
    "no_po_first_invoice",
    "no_purchase_order",
    "payer_account_unclear",
]

GET_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES: Set[
    GetInvoiceResultBuyerInvoiceUnverifiedReason
] = {
    "debit_note",
    "no_billing_connection",
    "no_po_first_invoice",
    "no_purchase_order",
    "payer_account_unclear",
}


def check_get_invoice_result_buyer_invoice_unverified_reason(
    value: str,
) -> GetInvoiceResultBuyerInvoiceUnverifiedReason:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES!r}"
    )
