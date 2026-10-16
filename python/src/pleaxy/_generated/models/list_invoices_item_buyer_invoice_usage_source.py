from typing import Literal, Set, cast

ListInvoicesItemBuyerInvoiceUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

LIST_INVOICES_ITEM_BUYER_INVOICE_USAGE_SOURCE_VALUES: Set[
    ListInvoicesItemBuyerInvoiceUsageSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_list_invoices_item_buyer_invoice_usage_source(
    value: str,
) -> ListInvoicesItemBuyerInvoiceUsageSource:
    if value in LIST_INVOICES_ITEM_BUYER_INVOICE_USAGE_SOURCE_VALUES:
        return cast(ListInvoicesItemBuyerInvoiceUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_ITEM_BUYER_INVOICE_USAGE_SOURCE_VALUES!r}"
    )
