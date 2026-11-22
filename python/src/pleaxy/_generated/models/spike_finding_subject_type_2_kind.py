from typing import Literal, Set, cast

SpikeFindingSubjectType2Kind = Literal["cloud_account"]

SPIKE_FINDING_SUBJECT_TYPE_2_KIND_VALUES: Set[SpikeFindingSubjectType2Kind] = {
    "cloud_account",
}


def check_spike_finding_subject_type_2_kind(value: str) -> SpikeFindingSubjectType2Kind:
    if value in SPIKE_FINDING_SUBJECT_TYPE_2_KIND_VALUES:
        return cast(SpikeFindingSubjectType2Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_2_KIND_VALUES!r}"
    )
