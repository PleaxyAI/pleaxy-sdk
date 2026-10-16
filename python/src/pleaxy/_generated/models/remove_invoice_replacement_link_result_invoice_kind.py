from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultInvoiceKind = Literal["prepayment"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_INVOICE_KIND_VALUES: Set[
    RemoveInvoiceReplacementLinkResultInvoiceKind
] = {
    "prepayment",
}


def check_remove_invoice_replacement_link_result_invoice_kind(
    value: str,
) -> RemoveInvoiceReplacementLinkResultInvoiceKind:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_INVOICE_KIND_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_INVOICE_KIND_VALUES!r}"
    )
