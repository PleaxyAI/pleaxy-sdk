from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method = Literal[
    "ach", "card", "check", "credit", "nothing_due", "other", "wire"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "nothing_due",
    "other",
    "wire",
}


def check_create_invoice_result_supplier_invoice_withdrawn_payment_type_0_method(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES
    ):
        return cast(
            CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
