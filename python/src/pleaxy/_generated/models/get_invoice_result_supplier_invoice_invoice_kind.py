from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceInvoiceKind = Literal["prepayment"]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES: Set[
    GetInvoiceResultSupplierInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_get_invoice_result_supplier_invoice_invoice_kind(
    value: str,
) -> GetInvoiceResultSupplierInvoiceInvoiceKind:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
