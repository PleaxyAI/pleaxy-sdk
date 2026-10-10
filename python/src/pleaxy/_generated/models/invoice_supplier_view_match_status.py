from typing import Literal, Set, cast

InvoiceSupplierViewMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

INVOICE_SUPPLIER_VIEW_MATCH_STATUS_VALUES: Set[InvoiceSupplierViewMatchStatus] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_invoice_supplier_view_match_status(
    value: str,
) -> InvoiceSupplierViewMatchStatus:
    if value in INVOICE_SUPPLIER_VIEW_MATCH_STATUS_VALUES:
        return cast(InvoiceSupplierViewMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_MATCH_STATUS_VALUES!r}"
    )
