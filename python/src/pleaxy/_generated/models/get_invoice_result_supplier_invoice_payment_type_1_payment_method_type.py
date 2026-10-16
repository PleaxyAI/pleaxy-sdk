from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_get_invoice_result_supplier_invoice_payment_type_1_payment_method_type(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentType1PaymentMethodType:
    if (
        value
        in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(GetInvoiceResultSupplierInvoicePaymentType1PaymentMethodType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
