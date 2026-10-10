from typing import Literal, Set, cast

InvoiceSupplierViewWithdrawnPaymentType0Status = Literal["recorded"]

INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    InvoiceSupplierViewWithdrawnPaymentType0Status
] = {
    "recorded",
}


def check_invoice_supplier_view_withdrawn_payment_type_0_status(
    value: str,
) -> InvoiceSupplierViewWithdrawnPaymentType0Status:
    if value in INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(InvoiceSupplierViewWithdrawnPaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
