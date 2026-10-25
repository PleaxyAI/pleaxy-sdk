from typing import Literal, Set, cast

CloudConnectionBillingPreviousFinalizedInvoiceSource = Literal[
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
]

CLOUD_CONNECTION_BILLING_PREVIOUS_FINALIZED_INVOICE_SOURCE_VALUES: Set[
    CloudConnectionBillingPreviousFinalizedInvoiceSource
] = {
    "aws_invoice",
    "billing_export",
    "ea_balance",
    "mca_invoice",
    "osp_invoice",
    "usage_api_closed_month",
}


def check_cloud_connection_billing_previous_finalized_invoice_source(
    value: str,
) -> CloudConnectionBillingPreviousFinalizedInvoiceSource:
    if value in CLOUD_CONNECTION_BILLING_PREVIOUS_FINALIZED_INVOICE_SOURCE_VALUES:
        return cast(CloudConnectionBillingPreviousFinalizedInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_BILLING_PREVIOUS_FINALIZED_INVOICE_SOURCE_VALUES!r}"
    )
