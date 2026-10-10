from typing import Literal, Set, cast

PaymentHistoryEntryAction = Literal[
    "export_withdrawn",
    "exported",
    "record_withdrawn",
    "recorded",
    "stripe_failed",
    "stripe_released",
    "stripe_started",
    "stripe_succeeded",
]

PAYMENT_HISTORY_ENTRY_ACTION_VALUES: Set[PaymentHistoryEntryAction] = {
    "export_withdrawn",
    "exported",
    "record_withdrawn",
    "recorded",
    "stripe_failed",
    "stripe_released",
    "stripe_started",
    "stripe_succeeded",
}


def check_payment_history_entry_action(value: str) -> PaymentHistoryEntryAction:
    if value in PAYMENT_HISTORY_ENTRY_ACTION_VALUES:
        return cast(PaymentHistoryEntryAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PAYMENT_HISTORY_ENTRY_ACTION_VALUES!r}"
    )
