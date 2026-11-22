from typing import Literal, Set, cast

PaceFindingSubjectType0Kind = Literal["ai_invoicer"]

PACE_FINDING_SUBJECT_TYPE_0_KIND_VALUES: Set[PaceFindingSubjectType0Kind] = {
    "ai_invoicer",
}


def check_pace_finding_subject_type_0_kind(value: str) -> PaceFindingSubjectType0Kind:
    if value in PACE_FINDING_SUBJECT_TYPE_0_KIND_VALUES:
        return cast(PaceFindingSubjectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_0_KIND_VALUES!r}"
    )
