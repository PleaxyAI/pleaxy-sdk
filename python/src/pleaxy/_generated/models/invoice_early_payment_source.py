from typing import Literal, Set, cast

InvoiceEarlyPaymentSource = Literal["contract", "supplier_offer"]

INVOICE_EARLY_PAYMENT_SOURCE_VALUES: Set[InvoiceEarlyPaymentSource] = {
    "contract",
    "supplier_offer",
}


def check_invoice_early_payment_source(value: str) -> InvoiceEarlyPaymentSource:
    if value in INVOICE_EARLY_PAYMENT_SOURCE_VALUES:
        return cast(InvoiceEarlyPaymentSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_EARLY_PAYMENT_SOURCE_VALUES!r}"
    )
