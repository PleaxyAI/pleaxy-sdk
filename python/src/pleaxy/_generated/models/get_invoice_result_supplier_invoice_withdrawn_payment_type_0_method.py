from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method = Literal[
    "ach", "card", "check", "credit", "other", "wire"
]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES: Set[
    GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method
] = {
    "ach",
    "card",
    "check",
    "credit",
    "other",
    "wire",
}


def check_get_invoice_result_supplier_invoice_withdrawn_payment_type_0_method(
    value: str,
) -> GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method:
    if (
        value
        in GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES
    ):
        return cast(GetInvoiceResultSupplierInvoiceWithdrawnPaymentType0Method, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_METHOD_VALUES!r}"
    )
