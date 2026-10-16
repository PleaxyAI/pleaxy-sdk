from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceSource = Literal[
    "direct", "feed", "manual", "po-flip"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceSource
] = {
    "direct",
    "feed",
    "manual",
    "po-flip",
}


def check_create_invoice_result_supplier_invoice_source(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceSource:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SOURCE_VALUES!r}"
    )
