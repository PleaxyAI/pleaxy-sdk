from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultReceiptCheckSkippedReason = Literal["small_invoice"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES: Set[
    AddInvoiceReplacementLinksResultReceiptCheckSkippedReason
] = {
    "small_invoice",
}


def check_add_invoice_replacement_links_result_receipt_check_skipped_reason(
    value: str,
) -> AddInvoiceReplacementLinksResultReceiptCheckSkippedReason:
    if (
        value
        in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES
    ):
        return cast(AddInvoiceReplacementLinksResultReceiptCheckSkippedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_RECEIPT_CHECK_SKIPPED_REASON_VALUES!r}"
    )
