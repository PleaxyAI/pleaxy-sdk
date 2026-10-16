from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultUsageSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_USAGE_SOURCE_VALUES: Set[
    AddInvoiceReplacementLinksResultUsageSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_add_invoice_replacement_links_result_usage_source(
    value: str,
) -> AddInvoiceReplacementLinksResultUsageSource:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_USAGE_SOURCE_VALUES:
        return cast(AddInvoiceReplacementLinksResultUsageSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_USAGE_SOURCE_VALUES!r}"
    )
