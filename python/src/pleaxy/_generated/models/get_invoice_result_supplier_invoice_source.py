from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceSource = Literal["direct", "feed", "manual", "po-flip"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES: Set[
    GetInvoiceResultSupplierInvoiceSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_get_invoice_result_supplier_invoice_source(
    value: str,
) -> GetInvoiceResultSupplierInvoiceSource:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES!r}"
    )
