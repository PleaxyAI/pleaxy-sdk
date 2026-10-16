from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1State = Literal[
    "processing", "succeeded"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1State
] = {
    "processing",
    "succeeded",
}


def check_create_invoice_result_supplier_invoice_withdrawn_payment_type_1_state(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1State:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES
    ):
        return cast(CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1State, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATE_VALUES!r}"
    )
