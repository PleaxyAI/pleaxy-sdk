from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceDueDateSource = Literal["default", "stated"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_create_invoice_result_supplier_invoice_due_date_source(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceDueDateSource:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
