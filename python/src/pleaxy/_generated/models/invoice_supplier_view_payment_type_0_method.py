from typing import Literal, Set, cast

InvoiceSupplierViewPaymentType0Method = Literal[
    "ach", "card", "check", "credit", "other", "wire"
]

INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    InvoiceSupplierViewPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "other",
    "wire",
}


def check_invoice_supplier_view_payment_type_0_method(
    value: str,
) -> InvoiceSupplierViewPaymentType0Method:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(InvoiceSupplierViewPaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
