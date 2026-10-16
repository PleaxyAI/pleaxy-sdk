from typing import Literal, Set, cast

RecordPaymentResultInvoiceKind = Literal["prepayment"]

RECORD_PAYMENT_RESULT_INVOICE_KIND_VALUES: Set[RecordPaymentResultInvoiceKind] = {
    "prepayment",
}


def check_record_payment_result_invoice_kind(
    value: str,
) -> RecordPaymentResultInvoiceKind:
    if value in RECORD_PAYMENT_RESULT_INVOICE_KIND_VALUES:
        return cast(RecordPaymentResultInvoiceKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_INVOICE_KIND_VALUES!r}"
    )
