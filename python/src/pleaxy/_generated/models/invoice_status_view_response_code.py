from typing import Literal, Set, cast

InvoiceStatusViewResponseCode = Literal["AB", "AP", "IP", "PD", "RE", "UQ"]

INVOICE_STATUS_VIEW_RESPONSE_CODE_VALUES: Set[InvoiceStatusViewResponseCode] = {
    "AB",
    "AP",
    "IP",
    "PD",
    "RE",
    "UQ",
}


def check_invoice_status_view_response_code(
    value: str,
) -> InvoiceStatusViewResponseCode:
    if value in INVOICE_STATUS_VIEW_RESPONSE_CODE_VALUES:
        return cast(InvoiceStatusViewResponseCode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VIEW_RESPONSE_CODE_VALUES!r}"
    )
