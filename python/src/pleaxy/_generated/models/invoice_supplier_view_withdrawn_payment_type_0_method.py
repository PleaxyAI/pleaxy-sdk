from typing import Literal, Set, cast

InvoiceSupplierViewWithdrawnPaymentType0Method = Literal[
    "ach", "card", "check", "other", "wire"
]

INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    InvoiceSupplierViewWithdrawnPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "other",
    "wire",
}


def check_invoice_supplier_view_withdrawn_payment_type_0_method(
    value: str,
) -> InvoiceSupplierViewWithdrawnPaymentType0Method:
    if value in INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(InvoiceSupplierViewWithdrawnPaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
