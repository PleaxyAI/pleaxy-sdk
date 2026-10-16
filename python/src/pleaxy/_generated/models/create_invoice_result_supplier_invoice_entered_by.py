from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceEnteredBy = Literal["buyer", "supplier"]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceEnteredBy
] = {
    "buyer",
    "supplier",
}


def check_create_invoice_result_supplier_invoice_entered_by(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceEnteredBy:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceEnteredBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_ENTERED_BY_VALUES!r}"
    )
