from typing import Literal, Set, cast

PaceFindingSubjectType3Kind = Literal["cloud_service"]

PACE_FINDING_SUBJECT_TYPE_3_KIND_VALUES: Set[PaceFindingSubjectType3Kind] = {
    "cloud_service",
}


def check_pace_finding_subject_type_3_kind(value: str) -> PaceFindingSubjectType3Kind:
    if value in PACE_FINDING_SUBJECT_TYPE_3_KIND_VALUES:
        return cast(PaceFindingSubjectType3Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_3_KIND_VALUES!r}"
    )
