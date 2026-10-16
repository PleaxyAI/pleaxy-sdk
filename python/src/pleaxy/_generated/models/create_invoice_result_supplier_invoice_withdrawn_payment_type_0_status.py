from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Status = Literal["recorded"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Status
] = {
    "recorded",
}


def check_create_invoice_result_supplier_invoice_withdrawn_payment_type_0_status(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Status:
    if (
        value
        in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES
    ):
        return cast(
            CreateInvoiceResultSupplierInvoiceWithdrawnPaymentType0Status, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_WITHDRAWN_PAYMENT_TYPE_0_STATUS_VALUES!r}"
    )
