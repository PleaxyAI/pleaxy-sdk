from typing import Literal, Set, cast

InvoicePaymentRecordStatus = Literal["exported", "recorded", "stripe"]

INVOICE_PAYMENT_RECORD_STATUS_VALUES: Set[InvoicePaymentRecordStatus] = {
    "exported",
    "recorded",
    "stripe",
}


def check_invoice_payment_record_status(value: str) -> InvoicePaymentRecordStatus:
    if value in INVOICE_PAYMENT_RECORD_STATUS_VALUES:
        return cast(InvoicePaymentRecordStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_PAYMENT_RECORD_STATUS_VALUES!r}"
    )
