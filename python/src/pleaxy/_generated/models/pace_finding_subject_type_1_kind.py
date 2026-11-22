from typing import Literal, Set, cast

PaceFindingSubjectType1Kind = Literal["ai_model"]

PACE_FINDING_SUBJECT_TYPE_1_KIND_VALUES: Set[PaceFindingSubjectType1Kind] = {
    "ai_model",
}


def check_pace_finding_subject_type_1_kind(value: str) -> PaceFindingSubjectType1Kind:
    if value in PACE_FINDING_SUBJECT_TYPE_1_KIND_VALUES:
        return cast(PaceFindingSubjectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_1_KIND_VALUES!r}"
    )
