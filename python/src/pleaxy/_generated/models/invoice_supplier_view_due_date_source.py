from typing import Literal, Set, cast

InvoiceSupplierViewDueDateSource = Literal["default", "stated"]

INVOICE_SUPPLIER_VIEW_DUE_DATE_SOURCE_VALUES: Set[InvoiceSupplierViewDueDateSource] = {
    "default",
    "stated",
}


def check_invoice_supplier_view_due_date_source(
    value: str,
) -> InvoiceSupplierViewDueDateSource:
    if value in INVOICE_SUPPLIER_VIEW_DUE_DATE_SOURCE_VALUES:
        return cast(InvoiceSupplierViewDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_DUE_DATE_SOURCE_VALUES!r}"
    )
