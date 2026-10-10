from typing import Literal, Set, cast

InvoiceRateWarningObject = Literal["payment", "tax"]

INVOICE_RATE_WARNING_OBJECT_VALUES: Set[InvoiceRateWarningObject] = {
    "payment",
    "tax",
}


def check_invoice_rate_warning_object(value: str) -> InvoiceRateWarningObject:
    if value in INVOICE_RATE_WARNING_OBJECT_VALUES:
        return cast(InvoiceRateWarningObject, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_RATE_WARNING_OBJECT_VALUES!r}"
    )
