from typing import Literal, Set, cast

InvoiceSupplierViewWithdrawnPaymentType1State = Literal["processing", "succeeded"]

INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES: Set[
    InvoiceSupplierViewWithdrawnPaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_invoice_supplier_view_withdrawn_payment_type_1_state(
    value: str,
) -> InvoiceSupplierViewWithdrawnPaymentType1State:
    if value in INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(InvoiceSupplierViewWithdrawnPaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
