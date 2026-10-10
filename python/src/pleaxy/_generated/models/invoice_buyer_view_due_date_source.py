from typing import Literal, Set, cast

InvoiceBuyerViewDueDateSource = Literal["default", "stated"]

INVOICE_BUYER_VIEW_DUE_DATE_SOURCE_VALUES: Set[InvoiceBuyerViewDueDateSource] = {
    "default",
    "stated",
}


def check_invoice_buyer_view_due_date_source(
    value: str,
) -> InvoiceBuyerViewDueDateSource:
    if value in INVOICE_BUYER_VIEW_DUE_DATE_SOURCE_VALUES:
        return cast(InvoiceBuyerViewDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_BUYER_VIEW_DUE_DATE_SOURCE_VALUES!r}"
    )
