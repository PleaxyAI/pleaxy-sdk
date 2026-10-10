from typing import Literal, Set, cast

InvoiceBuyerViewMatchBasis = Literal["purchase_order"]

INVOICE_BUYER_VIEW_MATCH_BASIS_VALUES: Set[InvoiceBuyerViewMatchBasis] = {
    "purchase_order",
}


def check_invoice_buyer_view_match_basis(value: str) -> InvoiceBuyerViewMatchBasis:
    if value in INVOICE_BUYER_VIEW_MATCH_BASIS_VALUES:
        return cast(InvoiceBuyerViewMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_MATCH_BASIS_VALUES!r}"
    )
