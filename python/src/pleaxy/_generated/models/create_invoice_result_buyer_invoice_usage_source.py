from typing import Literal, Set, cast

CreateInvoiceResultBuyerInvoiceUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

CREATE_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES: Set[
    CreateInvoiceResultBuyerInvoiceUsageSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_create_invoice_result_buyer_invoice_usage_source(
    value: str,
) -> CreateInvoiceResultBuyerInvoiceUsageSource:
    if value in CREATE_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES:
        return cast(CreateInvoiceResultBuyerInvoiceUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_BUYER_INVOICE_USAGE_SOURCE_VALUES!r}"
    )
