from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceSubmittedFormat = Literal["cxml", "json", "ubl"]

LIST_INVOICES_ITEM_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    ListInvoicesItemBuyerInvoiceSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_list_invoices_item_buyer_invoice_submitted_format(
    value: str,
) -> ListInvoicesItemBuyerInvoiceSubmittedFormat:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
