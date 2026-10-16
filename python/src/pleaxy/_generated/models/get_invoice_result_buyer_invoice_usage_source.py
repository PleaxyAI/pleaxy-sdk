from typing import Literal, Set, cast

GetInvoiceResultBuyerInvoiceUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

GET_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES: Set[
    GetInvoiceResultBuyerInvoiceUsageSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_get_invoice_result_buyer_invoice_usage_source(
    value: str,
) -> GetInvoiceResultBuyerInvoiceUsageSource:
    if value in GET_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES:
        return cast(GetInvoiceResultBuyerInvoiceUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES!r}"
    )
