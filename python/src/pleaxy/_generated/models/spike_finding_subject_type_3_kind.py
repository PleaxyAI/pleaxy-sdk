from typing import Literal, Set, cast

SpikeFindingSubjectType3Kind = Literal["cloud_service"]

SPIKE_FINDING_SUBJECT_TYPE_3_KIND_VALUES: Set[SpikeFindingSubjectType3Kind] = {
    "cloud_service",
}


def check_spike_finding_subject_type_3_kind(value: str) -> SpikeFindingSubjectType3Kind:
    if value in SPIKE_FINDING_SUBJECT_TYPE_3_KIND_VALUES:
        return cast(SpikeFindingSubjectType3Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_3_KIND_VALUES!r}"
    )
