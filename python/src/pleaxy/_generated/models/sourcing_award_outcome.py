from typing import Literal, Set, cast

SourcingAwardOutcome = Literal["both", "contract", "order"]

SOURCING_AWARD_OUTCOME_VALUES: Set[SourcingAwardOutcome] = {
    "both",
    "contract",
    "order",
}


def check_sourcing_award_outcome(value: str) -> SourcingAwardOutcome:
    if value in SOURCING_AWARD_OUTCOME_VALUES:
        return cast(SourcingAwardOutcome, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_AWARD_OUTCOME_VALUES!r}"
    )
