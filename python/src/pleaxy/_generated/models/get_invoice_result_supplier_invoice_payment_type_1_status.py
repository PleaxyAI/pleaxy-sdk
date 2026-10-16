from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoicePaymentType1Status = Literal["stripe"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    GetInvoiceResultSupplierInvoicePaymentType1Status
] = {
    "stripe",
}


def check_get_invoice_result_supplier_invoice_payment_type_1_status(
    value: str,
) -> GetInvoiceResultSupplierInvoicePaymentType1Status:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES:
        return cast(GetInvoiceResultSupplierInvoicePaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
