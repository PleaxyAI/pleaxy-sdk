from typing import Literal, Set, cast

InvoiceBuyerViewUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

INVOICE_BUYER_VIEW_USAGE_SOURCE_VALUES: Set[InvoiceBuyerViewUsageSource] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_invoice_buyer_view_usage_source(value: str) -> InvoiceBuyerViewUsageSource:
    if value in INVOICE_BUYER_VIEW_USAGE_SOURCE_VALUES:
        return cast(InvoiceBuyerViewUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_USAGE_SOURCE_VALUES!r}"
    )
