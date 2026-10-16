from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultUnverifiedReason = Literal[
    "debit_note", "no_billing_connection", "no_purchase_order"
]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_UNVERIFIED_REASON_VALUES: Set[
    AddInvoiceReplacementLinksResultUnverifiedReason
] = {
    "debit_note",
    "no_billing_connection",
    "no_purchase_order",
}


def check_add_invoice_replacement_links_result_unverified_reason(
    value: str,
) -> AddInvoiceReplacementLinksResultUnverifiedReason:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_UNVERIFIED_REASON_VALUES:
        return cast(AddInvoiceReplacementLinksResultUnverifiedReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_UNVERIFIED_REASON_VALUES!r}"
    )
