from typing import Literal, Set, cast

InvoiceSupplierViewPaymentType1PaymentMethodType = Literal["card", "us_bank_account"]

INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    InvoiceSupplierViewPaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_invoice_supplier_view_payment_type_1_payment_method_type(
    value: str,
) -> InvoiceSupplierViewPaymentType1PaymentMethodType:
    if value in INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES:
        return cast(InvoiceSupplierViewPaymentType1PaymentMethodType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_SUPPLIER_VIEW_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
