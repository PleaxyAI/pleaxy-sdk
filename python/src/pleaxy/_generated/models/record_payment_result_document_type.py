from typing import Literal, Set, cast

RecordPaymentResultDocumentType = Literal["debit_note"]

RECORD_PAYMENT_RESULT_DOCUMENT_TYPE_VALUES: Set[RecordPaymentResultDocumentType] = {
    "debit_note",
}


def check_record_payment_result_document_type(
    value: str,
) -> RecordPaymentResultDocumentType:
    if value in RECORD_PAYMENT_RESULT_DOCUMENT_TYPE_VALUES:
        return cast(RecordPaymentResultDocumentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORD_PAYMENT_RESULT_DOCUMENT_TYPE_VALUES!r}"
    )
