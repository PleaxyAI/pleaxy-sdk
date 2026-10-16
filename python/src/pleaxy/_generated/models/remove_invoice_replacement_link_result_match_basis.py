from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultMatchBasis = Literal["purchase_order"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_BASIS_VALUES: Set[
    RemoveInvoiceReplacementLinkResultMatchBasis
] = {
    "purchase_order",
}


def check_remove_invoice_replacement_link_result_match_basis(
    value: str,
) -> RemoveInvoiceReplacementLinkResultMatchBasis:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_BASIS_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultMatchBasis, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_MATCH_BASIS_VALUES!r}"
    )
