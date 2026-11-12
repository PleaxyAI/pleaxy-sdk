from typing import Literal, Set, cast

ListAvailableCreditsResultLocked = Literal[
    "exported", "otherCurrency", "paid", "rejected"
]

LIST_AVAILABLE_CREDITS_RESULT_LOCKED_VALUES: Set[ListAvailableCreditsResultLocked] = {
    "exported",
    "otherCurrency",
    "paid",
    "rejected",
}


def check_list_available_credits_result_locked(
    value: str,
) -> ListAvailableCreditsResultLocked:
    if value in LIST_AVAILABLE_CREDITS_RESULT_LOCKED_VALUES:
        return cast(ListAvailableCreditsResultLocked, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AVAILABLE_CREDITS_RESULT_LOCKED_VALUES!r}"
    )
