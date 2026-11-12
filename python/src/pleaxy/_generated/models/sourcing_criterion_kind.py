from typing import Literal, Set, cast

SourcingCriterionKind = Literal["evaluators", "price", "questionnaire"]

SOURCING_CRITERION_KIND_VALUES: Set[SourcingCriterionKind] = {
    "evaluators",
    "price",
    "questionnaire",
}


def check_sourcing_criterion_kind(value: str) -> SourcingCriterionKind:
    if value in SOURCING_CRITERION_KIND_VALUES:
        return cast(SourcingCriterionKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_CRITERION_KIND_VALUES!r}"
    )
