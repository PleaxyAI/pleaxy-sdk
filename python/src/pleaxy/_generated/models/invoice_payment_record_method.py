from typing import Literal, Set, cast

InvoicePaymentRecordMethod = Literal["ach", "card", "check", "other", "wire"]

INVOICE_PAYMENT_RECORD_METHOD_VALUES: Set[InvoicePaymentRecordMethod] = {
    "ach",
    "card",
    "check",
    "other",
    "wire",
}


def check_invoice_payment_record_method(value: str) -> InvoicePaymentRecordMethod:
    if value in INVOICE_PAYMENT_RECORD_METHOD_VALUES:
        return cast(InvoicePaymentRecordMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_RECORD_METHOD_VALUES!r}"
    )
