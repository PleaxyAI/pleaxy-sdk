from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceReceiptCheckSkippedReason = Literal["small_invoice"]

LIST_INVOICES_ITEM_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    ListInvoicesItemBuyerInvoiceReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_list_invoices_item_buyer_invoice_receipt_check_skipped_reason(
    value: str,
) -> ListInvoicesItemBuyerInvoiceReceiptCheckSkippedReason:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
