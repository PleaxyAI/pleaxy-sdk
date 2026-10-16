from typing import Literal, Set, cast

AddInvoiceReplacementLinksResultDiscrepancyReason = Literal[
    "amount", "controls", "currency"
]

ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DISCREPANCY_REASON_VALUES: Set[
    AddInvoiceReplacementLinksResultDiscrepancyReason
] = {
    "amount",
    "controls",
    "currency",
}


def check_add_invoice_replacement_links_result_discrepancy_reason(
    value: str,
) -> AddInvoiceReplacementLinksResultDiscrepancyReason:
    if value in ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DISCREPANCY_REASON_VALUES:
        return cast(AddInvoiceReplacementLinksResultDiscrepancyReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADD_INVOICE_REPLACEMENT_LINKS_RESULT_DISCREPANCY_REASON_VALUES!r}"
    )
