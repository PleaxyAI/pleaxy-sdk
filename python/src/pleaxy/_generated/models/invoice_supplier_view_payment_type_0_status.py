from typing import Literal, Set, cast

InvoiceSupplierViewPaymentType0Status = Literal["recorded"]

INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    InvoiceSupplierViewPaymentType0Status
] = {
    "recorded",
}


def check_invoice_supplier_view_payment_type_0_status(
    value: str,
) -> InvoiceSupplierViewPaymentType0Status:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(InvoiceSupplierViewPaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
