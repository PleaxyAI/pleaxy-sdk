from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceInvoiceKind = Literal["prepayment"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceInvoiceKind
] = {
    "prepayment",
}


def check_create_invoice_result_supplier_invoice_invoice_kind(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceInvoiceKind:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_INVOICE_KIND_VALUES!r}"
    )
