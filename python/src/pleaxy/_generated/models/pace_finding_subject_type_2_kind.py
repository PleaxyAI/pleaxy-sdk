from typing import Literal, Set, cast

PaceFindingSubjectType2Kind = Literal["cloud_account"]

PACE_FINDING_SUBJECT_TYPE_2_KIND_VALUES: Set[PaceFindingSubjectType2Kind] = {
    "cloud_account",
}


def check_pace_finding_subject_type_2_kind(value: str) -> PaceFindingSubjectType2Kind:
    if value in PACE_FINDING_SUBJECT_TYPE_2_KIND_VALUES:
        return cast(PaceFindingSubjectType2Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_2_KIND_VALUES!r}"
    )
