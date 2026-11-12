from typing import Literal, Set, cast

SourcingComparisonResponderAnsweredVia = Literal["link"]

SOURCING_COMPARISON_RESPONDER_ANSWERED_VIA_VALUES: Set[
    SourcingComparisonResponderAnsweredVia
] = {
    "link",
}


def check_sourcing_comparison_responder_answered_via(
    value: str,
) -> SourcingComparisonResponderAnsweredVia:
    if value in SOURCING_COMPARISON_RESPONDER_ANSWERED_VIA_VALUES:
        return cast(SourcingComparisonResponderAnsweredVia, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_RESPONDER_ANSWERED_VIA_VALUES!r}"
    )
