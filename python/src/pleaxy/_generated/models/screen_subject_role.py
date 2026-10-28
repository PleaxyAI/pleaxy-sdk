from typing import Literal, Set, cast

ScreenSubjectRole = Literal["former_name", "name", "payee"]

SCREEN_SUBJECT_ROLE_VALUES: Set[ScreenSubjectRole] = {
    "former_name",
    "name",
    "payee",
}


def check_screen_subject_role(value: str) -> ScreenSubjectRole:
    if value in SCREEN_SUBJECT_ROLE_VALUES:
        return cast(ScreenSubjectRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCREEN_SUBJECT_ROLE_VALUES!r}"
    )
