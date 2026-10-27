from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceUnverifiedReason = Literal[
    "debit_note",
    "no_billing_connection",
    "no_po_first_invoice",
    "no_purchase_order",
    "payer_account_unclear",
]

CREATE_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceUnverifiedReason
] = {
    "debit_note",
    "no_billing_connection",
    "no_po_first_invoice",
    "no_purchase_order",
    "payer_account_unclear",
}


def check_create_invoice_result_buyer_invoice_unverified_reason(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceUnverifiedReason:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_UNVERIFIED_REASON_VALUES!r}"
    )
