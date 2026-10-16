from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_USAGE_SOURCE_VALUES: Set[
    RemoveInvoiceReplacementLinkResultUsageSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_remove_invoice_replacement_link_result_usage_source(
    value: str,
) -> RemoveInvoiceReplacementLinkResultUsageSource:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_USAGE_SOURCE_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_USAGE_SOURCE_VALUES!r}"
    )
