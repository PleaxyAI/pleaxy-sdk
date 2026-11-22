from typing import Literal, Set, cast

SpikeFindingSubjectType3Provider = Literal["aws", "azure", "gcp", "oci"]

SPIKE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES: Set[SpikeFindingSubjectType3Provider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_spike_finding_subject_type_3_provider(
    value: str,
) -> SpikeFindingSubjectType3Provider:
    if value in SPIKE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES:
        return cast(SpikeFindingSubjectType3Provider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES!r}"
    )
