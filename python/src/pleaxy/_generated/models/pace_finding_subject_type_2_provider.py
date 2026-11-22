from typing import Literal, Set, cast

PaceFindingSubjectType2Provider = Literal["aws", "azure", "gcp", "oci"]

PACE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES: Set[PaceFindingSubjectType2Provider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_pace_finding_subject_type_2_provider(
    value: str,
) -> PaceFindingSubjectType2Provider:
    if value in PACE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES:
        return cast(PaceFindingSubjectType2Provider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_2_PROVIDER_VALUES!r}"
    )
