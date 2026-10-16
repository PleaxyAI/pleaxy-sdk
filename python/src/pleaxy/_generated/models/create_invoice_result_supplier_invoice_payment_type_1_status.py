from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentType1Status = Literal["stripe"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentType1Status
] = {
    "stripe",
}


def check_create_invoice_result_supplier_invoice_payment_type_1_status(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentType1Status:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(CreateInvoiceResultSupplierInvoicePaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
