from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentType0Method = Literal[
    "ach", "card", "check", "credit", "nothing_due", "other", "wire"
]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "nothing_due",
    "other",
    "wire",
}


def check_get_invoice_result_supplier_invoice_payment_type_0_method(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentType0Method:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES:
        return cast(GetInvoiceResultSupplierInvoicePaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
