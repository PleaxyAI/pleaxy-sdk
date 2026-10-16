from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1PaymentMethodType = Literal[
    "card", "us_bank_account"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1PaymentMethodType
] = {
    "card",
    "us_bank_account",
}


def check_create_invoice_result_supplier_invoice_withdrawn_payment_type_1_payment_method_type(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1PaymentMethodType:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES
    ):
        return cast(
            CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1PaymentMethodType,
            value,
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_PAYMENT_METHOD_TYPE_VALUES!r}"
    )
