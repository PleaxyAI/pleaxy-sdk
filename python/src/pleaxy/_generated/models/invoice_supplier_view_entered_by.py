from typing import Literal, Set, cast

InvoiceSupplierViewEnteredBy = Literal["buyer", "supplier"]

INVOICE_SUPPLIER_VIEW_ENTERED_BY_VALUES: Set[InvoiceSupplierViewEnteredBy] = {
    "buyer",
    "supplier",
}


def check_invoice_supplier_view_entered_by(value: str) -> InvoiceSupplierViewEnteredBy:
    if value in INVOICE_SUPPLIER_VIEW_ENTERED_BY_VALUES:
        return cast(InvoiceSupplierViewEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_ENTERED_BY_VALUES!r}"
    )
