from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status = Literal["stripe"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status
] = {
    "stripe",
}


def check_create_invoice_result_supplier_invoice_withdrawn_payment_type_1_status(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES
    ):
        return cast(
            CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType1Status, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_1_STATUS_VALUES!r}"
    )
