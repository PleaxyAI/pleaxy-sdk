from typing import Literal, Set, cast

SpikeFindingSubjectType2Provider = Literal["aws", "azure", "gcp", "oci"]

SPIKE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES: Set[SpikeFindingSubjectType2Provider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_spike_finding_subject_type_2_provider(
    value: str,
) -> SpikeFindingSubjectType2Provider:
    if value in SPIKE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES:
        return cast(SpikeFindingSubjectType2Provider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES!r}"
    )
