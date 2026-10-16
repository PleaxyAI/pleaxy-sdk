from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceDueDateSource = Literal["default", "stated"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES: Set[
    GetInvoiceResultSupplierInvoiceDueDateSource
] = {
    "default",
    "stated",
}


def check_get_invoice_result_supplier_invoice_due_date_source(
    value: str,
) -> GetInvoiceResultSupplierInvoiceDueDateSource:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceDueDateSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_DUE_DATE_SOURCE_VALUES!r}"
    )
