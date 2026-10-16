from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentType0Method = Literal[
    "ach", "card", "check", "credit", "other", "wire"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "other",
    "wire",
}


def check_create_invoice_result_supplier_invoice_payment_type_0_method(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentType0Method:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(CreateInvoiceResultSupplierInvoicePaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
