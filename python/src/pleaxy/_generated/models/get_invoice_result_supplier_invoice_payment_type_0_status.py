from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentType0Status = Literal["recorded"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentType0Status
] = {
    "recorded",
}


def check_get_invoice_result_supplier_invoice_payment_type_0_status(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentType0Status:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES:
        return cast(GetInvoiceResultSupplierInvoicePaymentType0Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
