from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_create_invoice_result_supplier_invoice_payment_type_1_payment_method_type(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentType1PaymentMethodType:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(
            CreateInvoiceResultSupplierInvoicePaymentType1PaymentMethodType, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
