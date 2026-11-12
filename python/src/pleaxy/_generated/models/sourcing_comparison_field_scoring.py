from typing import Literal, Set, cast

SourcingComparisonFieldScoring = Literal["choice", "manual"]

SOURCING_COMPARISON_FIELD_SCORING_VALUES: Set[SourcingComparisonFieldScoring] = {
    "choice",
    "manual",
}


def check_sourcing_comparison_field_scoring(
    value: str,
) -> SourcingComparisonFieldScoring:
    if value in SOURCING_COMPARISON_FIELD_SCORING_VALUES:
        return cast(SourcingComparisonFieldScoring, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_FIELD_SCORING_VALUES!r}"
    )
