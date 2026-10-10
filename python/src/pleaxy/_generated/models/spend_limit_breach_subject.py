from typing import Literal, Set, cast

SpendLimitBreachSubject = Literal["actor", "requester"]

SPEND_LIMIT_BREACH_SUBJECT_VALUES: Set[SpendLimitBreachSubject] = {
    "actor",
    "requester",
}


def check_spend_limit_breach_subject(value: str) -> SpendLimitBreachSubject:
    if value in SPEND_LIMIT_BREACH_SUBJECT_VALUES:
        return cast(SpendLimitBreachSubject, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPEND_LIMIT_BREACH_SUBJECT_VALUES!r}"
    )
