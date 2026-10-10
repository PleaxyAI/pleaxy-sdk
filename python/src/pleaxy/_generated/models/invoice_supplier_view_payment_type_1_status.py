from typing import Literal, Set, cast

InvoiceSupplierViewPaymentType1Status = Literal["stripe"]

INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    InvoiceSupplierViewPaymentType1Status
] = {
    "stripe",
}


def check_invoice_supplier_view_payment_type_1_status(
    value: str,
) -> InvoiceSupplierViewPaymentType1Status:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(InvoiceSupplierViewPaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
