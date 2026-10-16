from typing import Literal, Set, cast

CreateInvoiceResultSupplierInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES: Set[
    CreateInvoiceResultSupplierInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_create_invoice_result_supplier_invoice_match_status(
    value: str,
) -> CreateInvoiceResultSupplierInvoiceMatchStatus:
    if value in CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES:
        return cast(CreateInvoiceResultSupplierInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
