from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status = Literal["stripe"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status
] = {
    "stripe",
}


def check_get_invoice_result_supplier_invoice_withdrawn_payment_type_1_status(
    value: str,
) -> GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status:
    if (
        value
        in GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES
    ):
        return cast(GetInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
