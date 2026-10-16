from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultInvoiceKind = Literal["prepayment"]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_INVOICE_KIND_VALUES: Set[
    AddInvoiceReplacementLinksResultInvoiceKind
] = {
    "prepayment",
}


def check_add_invoice_replacement_links_result_invoice_kind(
    value: str,
) -> AddInvoiceReplacementLinksResultInvoiceKind:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_INVOICE_KIND_VALUES:
        return cast(AddInvoiceReplacementLinksResultInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_INVOICE_KIND_VALUES!r}"
    )
