from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentType1State = Literal["processing", "succeeded"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_create_invoice_result_supplier_invoice_payment_type_1_state(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentType1State:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES:
        return cast(CreateInvoiceResultSupplierInvoicePaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
