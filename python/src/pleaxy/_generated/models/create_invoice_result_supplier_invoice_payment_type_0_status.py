from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoicePaymentType0Status = Literal["recorded"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierInvoicePaymentType0Status
] = {
    "recorded",
}


def check_create_invoice_result_supplier_invoice_payment_type_0_status(
    value: str,
) -> CreateInvoiceResultSupplierInvoicePaymentType0Status:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(CreateInvoiceResultSupplierInvoicePaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
