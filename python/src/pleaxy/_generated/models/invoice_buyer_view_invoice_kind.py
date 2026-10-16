from typing import Literal, Set, cast

InvoiceBuyerViewInvoiceKind = Literal["prepayment"]

INVOICE_BUYER_VIEW_INVOICE_KIND_VALUES: Set[InvoiceBuyerViewInvoiceKind] = {
    "prepayment",
}


def check_invoice_buyer_view_invoice_kind(value: str) -> InvoiceBuyerViewInvoiceKind:
    if value in INVOICE_BUYER_VIEW_INVOICE_KIND_VALUES:
        return cast(InvoiceBuyerViewInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_INVOICE_KIND_VALUES!r}"
    )
