from typing import Literal, Set, cast

PaceFindingSubjectType3Provider = Literal["aws", "azure", "gcp", "oci"]

PACE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES: Set[PaceFindingSubjectType3Provider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_pace_finding_subject_type_3_provider(
    value: str,
) -> PaceFindingSubjectType3Provider:
    if value in PACE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES:
        return cast(PaceFindingSubjectType3Provider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PACE_FINDING_SUBJECT_TYPE_3_PROVIDER_VALUES!r}"
    )
