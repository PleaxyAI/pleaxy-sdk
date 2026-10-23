from typing import Literal, Set, cast

PaymentHistoryEntryRecordMethod = Literal[
    "ach", "card", "check", "credit", "nothing_due", "other", "wire"
]

PAYMENT_HISTORY_ENTRY_RECORD_METHOD_VALUES: Set[PaymentHistoryEntryRecordMethod] = {
    "ach",
    "card",
    "check",
    "credit",
    "nothing_due",
    "other",
    "wire",
}


def check_payment_history_entry_record_method(
    value: str,
) -> PaymentHistoryEntryRecordMethod:
    if value in PAYMENT_HISTORY_ENTRY_RECORD_METHOD_VALUES:
        return cast(PaymentHistoryEntryRecordMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_HISTORY_ENTRY_RECORD_METHOD_VALUES!r}"
    )
