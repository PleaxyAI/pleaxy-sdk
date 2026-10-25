from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceUnverifiedReason = Literal[
    "debit_note", "no_billing_connection", "no_purchase_order", "payer_account_unclear"
]

LIST_INVOICES_ITEM_BUYER_INVOICE_UNVERIFIED_REASON_VALUES: Set[
    ListInvoicesItemBuyerInvoiceUnverifiedReason
] = {
    "debit_note",
    "no_billing_connection",
    "no_purchase_order",
    "payer_account_unclear",
}


def check_list_invoices_item_buyer_invoice_unverified_reason(
    value: str,
) -> ListInvoicesItemBuyerInvoiceUnverifiedReason:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_UNVERIFIED_REASON_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_UNVERIFIED_REASON_VALUES!r}"
    )
