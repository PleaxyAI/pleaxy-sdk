from typing import Literal, Set, cast

RemoveInvoiceReplacementLinkResultEnteredBy = Literal["buyer", "supplier"]

REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_ENTERED_BY_VALUES: Set[
    RemoveInvoiceReplacementLinkResultEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_remove_invoice_replacement_link_result_entered_by(
    value: str,
) -> RemoveInvoiceReplacementLinkResultEnteredBy:
    if value in REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_ENTERED_BY_VALUES:
        return cast(RemoveInvoiceReplacementLinkResultEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMOVE_INVOICE_REPLACEMENT_LINK_RESULT_ENTERED_BY_VALUES!r}"
    )
