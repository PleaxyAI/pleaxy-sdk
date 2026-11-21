from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceSubmittedFormat = Literal[
    "cii", "cxml", "fatturapa", "json", "ubl"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceSubmittedFormat
] = {
    "cii",
    "cxml",
    "fatturapa",
    "json",
    "ubl",
}


def check_create_invoice_result_supplier_invoice_submitted_format(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceSubmittedFormat:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceSubmittedFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_SUBMITTED_FORMAT_VALUES!r}"
    )
