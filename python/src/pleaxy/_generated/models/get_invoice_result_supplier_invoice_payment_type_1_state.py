from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentType1State = Literal["processing", "succeeded"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_get_invoice_result_supplier_invoice_payment_type_1_state(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentType1State:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(GetInvoiceResultSupplierInvoicePaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
