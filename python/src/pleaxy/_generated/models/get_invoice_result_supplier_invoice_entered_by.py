from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceEnteredBy = Literal["buyer", "supplier"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES: Set[
    GetInvoiceResultSupplierInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_get_invoice_result_supplier_invoice_entered_by(
    value: str,
) -> GetInvoiceResultSupplierInvoiceEnteredBy:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES!r}"
    )
