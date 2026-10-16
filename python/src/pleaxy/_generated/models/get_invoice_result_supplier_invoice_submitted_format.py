from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceSubmittedFormat = Literal["cxml", "json", "ubl"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    GetInvoiceResultSupplierInvoiceSubmittedFormat
] = {
    "cxml",
    "json",
    "ubl",
}


def check_get_invoice_result_supplier_invoice_submitted_format(
    value: str,
) -> GetInvoiceResultSupplierInvoiceSubmittedFormat:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
