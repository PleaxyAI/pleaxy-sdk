from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultMatchBasis = Literal["no_po_history", "purchase_order"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_BASIS_VALUES: Set[
    AddInvoiceReplacementLinksResultMatchBasis
] = {
    "no_po_history",
    "purchase_order",
}


def check_add_invoice_replacement_links_result_match_basis(
    value: str,
) -> AddInvoiceReplacementLinksResultMatchBasis:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_BASIS_VALUES:
        return cast(AddInvoiceReplacementLinksResultMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_MATCH_BASIS_VALUES!r}"
    )
