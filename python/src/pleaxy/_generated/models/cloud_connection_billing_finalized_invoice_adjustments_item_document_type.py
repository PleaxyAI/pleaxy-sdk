from typing import Literal, Set, cast

CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType = Literal[
    "CreditNote", "VoidNote"
]

CLOUD_CONNECTION_BILLING_FINALIZED_INVOICE_ADJUSTMENTS_ITEM_DOCUMENT_TYPE_VALUES: Set[
    CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType
] = {
    "CreditNote",
    "VoidNote",
}


def check_cloud_connection_billing_finalized_invoice_adjustments_item_document_type(
    value: str,
) -> CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType:
    if (
        value
        in CLOUD_CONNECTION_BILLING_FINALIZED_INVOICE_ADJUSTMENTS_ITEM_DOCUMENT_TYPE_VALUES
    ):
        return cast(
            CloudConnectionBillingFinalizedInvoiceAdjustmentsItemDocumentType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_BILLING_FINALIZED_INVOICE_ADJUSTMENTS_ITEM_DOCUMENT_TYPE_VALUES!r}"
    )
