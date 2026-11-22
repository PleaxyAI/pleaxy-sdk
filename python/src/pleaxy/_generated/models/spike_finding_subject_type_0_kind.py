from typing import Literal, Set, cast

SpikeFindingSubjectType0Kind = Literal["ai_invoicer"]

SPIKE_FINDING_SUBJECT_TYPE_0_KIND_VALUES: Set[SpikeFindingSubjectType0Kind] = {
    "ai_invoicer",
}


def check_spike_finding_subject_type_0_kind(value: str) -> SpikeFindingSubjectType0Kind:
    if value in SPIKE_FINDING_SUBJECT_TYPE_0_KIND_VALUES:
        return cast(SpikeFindingSubjectType0Kind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_0_KIND_VALUES!r}"
    )
