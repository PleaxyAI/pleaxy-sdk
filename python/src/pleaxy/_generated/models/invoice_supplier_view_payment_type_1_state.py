from typing import Literal, Set, cast

InvoiceSupplierViewPaymentType1State = Literal["processing", "succeeded"]

INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATE_VALUES: Set[
    InvoiceSupplierViewPaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_invoice_supplier_view_payment_type_1_state(
    value: str,
) -> InvoiceSupplierViewPaymentType1State:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(InvoiceSupplierViewPaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
