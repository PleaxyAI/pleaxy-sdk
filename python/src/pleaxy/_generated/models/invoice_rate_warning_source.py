from typing import Literal, Set, cast

InvoiceRateWarningSource = Literal["override", "provider"]

INVOICE_RATE_WARNING_SOURCE_VALUES: Set[InvoiceRateWarningSource] = {
    "override",
    "provider",
}


def check_invoice_rate_warning_source(value: str) -> InvoiceRateWarningSource:
    if value in INVOICE_RATE_WARNING_SOURCE_VALUES:
        return cast(InvoiceRateWarningSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_RATE_WARNING_SOURCE_VALUES!r}"
    )
