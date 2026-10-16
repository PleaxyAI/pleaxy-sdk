from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1State = Literal[
    "processing", "succeeded"
]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES: Set[
    GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_get_invoice_result_supplier_invoice_withdrawn_payment_type_1_state(
    value: str,
) -> GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1State:
    if (
        value
        in GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES
    ):
        return cast(GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
