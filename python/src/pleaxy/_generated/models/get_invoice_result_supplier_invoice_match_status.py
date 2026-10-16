from typing import Literal, Set, cast

GetInvoiceResultSupplierInvoiceMatchStatus = Literal[
    "discrepancy", "matched", "pending", "unverified"
]

GET_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES: Set[
    GetInvoiceResultSupplierInvoiceMatchStatus
] = {
    "discrepancy",
    "matched",
    "pending",
    "unverified",
}


def check_get_invoice_result_supplier_invoice_match_status(
    value: str,
) -> GetInvoiceResultSupplierInvoiceMatchStatus:
    if value in GET_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES:
        return cast(GetInvoiceResultSupplierInvoiceMatchStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INVOICE_RESULT_SUPPLIER_INVOICE_MATCH_STATUS_VALUES!r}"
    )
