from typing import Literal, Set, cast

InvoiceSupplierViewWithdrawnPaymentType1Status = Literal["stripe"]

INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    InvoiceSupplierViewWithdrawnPaymentType1Status
] = {
    "stripe",
}


def check_invoice_supplier_view_withdrawn_payment_type_1_status(
    value: str,
) -> InvoiceSupplierViewWithdrawnPaymentType1Status:
    if value in INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(InvoiceSupplierViewWithdrawnPaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
