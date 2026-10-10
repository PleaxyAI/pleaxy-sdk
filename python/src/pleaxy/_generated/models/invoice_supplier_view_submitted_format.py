from typing import Literal, Set, cast

InvoiceSupplierViewSubmittedFormat = Literal["cxml", "json", "ubl"]

INVOICE_SUPPLIER_VIEW_SUBMITTED_FORMAT_VALUES: Set[
    InvoiceSupplierViewSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_invoice_supplier_view_submitted_format(
    value: str,
) -> InvoiceSupplierViewSubmittedFormat:
    if value in INVOICE_SUPPLIER_VIEW_SUBMITTED_FORMAT_VALUES:
        return cast(InvoiceSupplierViewSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_SUBMITTED_FORMAT_VALUES!r}"
    )
