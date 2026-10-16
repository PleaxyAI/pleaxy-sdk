from typing import Literal, Set, cast

InvoiceSupplierViewInvoiceKind = Literal["prepayment"]

INVOICE_SUPPLIER_VIEW_INVOICE_KIND_VALUES: Set[InvoiceSupplierViewInvoiceKind] = {
    "prepayment",
}


def check_invoice_supplier_view_invoice_kind(
    value: str,
) -> InvoiceSupplierViewInvoiceKind:
    if value in INVOICE_SUPPLIER_VIEW_INVOICE_KIND_VALUES:
        return cast(InvoiceSupplierViewInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_INVOICE_KIND_VALUES!r}"
    )
