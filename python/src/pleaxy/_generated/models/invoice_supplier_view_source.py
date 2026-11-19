from typing import Literal, Set, cast

InvoiceSupplierViewSource = Literal["cloud_sync", "direct", "feed", "manual", "po-flip"]

INVOICE_SUPPLIER_VIEW_SOURCE_VALUES: Set[InvoiceSupplierViewSource] = {
    "cloud_sync",
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_invoice_supplier_view_source(value: str) -> InvoiceSupplierViewSource:
    if value in INVOICE_SUPPLIER_VIEW_SOURCE_VALUES:
        return cast(InvoiceSupplierViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_SOURCE_VALUES!r}"
    )
