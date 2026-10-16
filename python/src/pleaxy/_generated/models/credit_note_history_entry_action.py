from typing import Literal, Set, cast

CreditNoteHistoryEntryAction = Literal[
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
]

CREDIT_NOTE_HISTORY_ENTRY_ACTION_VALUES: Set[CreditNoteHistoryEntryAction] = {
    "accepted",
    "applied",
    "exported",
    "issued",
    "rejected",
    "removed",
    "returned",
    "voided",
}


def check_credit_note_history_entry_action(value: str) -> CreditNoteHistoryEntryAction:
    if value in CREDIT_NOTE_HISTORY_ENTRY_ACTION_VALUES:
        return cast(CreditNoteHistoryEntryAction, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREDIT_NOTE_HISTORY_ENTRY_ACTION_VALUES!r}"
    )
