from typing import Literal, Set, cast

SpikeFindingSubjectType1Kind = Literal["ai_model"]

SPIKE_FINDING_SUBJECT_TYPE_1_KIND_VALUES: Set[SpikeFindingSubjectType1Kind] = {
    "ai_model",
}


def check_spike_finding_subject_type_1_kind(value: str) -> SpikeFindingSubjectType1Kind:
    if value in SPIKE_FINDING_SUBJECT_TYPE_1_KIND_VALUES:
        return cast(SpikeFindingSubjectType1Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_1_KIND_VALUES!r}"
    )
