from typing import Literal, Set, cast

SourcingComparisonResponderRiskLevel = Literal["attention", "blocked", "ok"]

SOURCING_COMPARISON_RESPONDER_RISK_LEVEL_VALUES: Set[
    SourcingComparisonResponderRiskLevel
] = {
    "attention",
    "blocked",
    "ok",
}


def check_sourcing_comparison_responder_risk_level(
    value: str,
) -> SourcingComparisonResponderRiskLevel:
    if value in SOURCING_COMPARISON_RESPONDER_RISK_LEVEL_VALUES:
        return cast(SourcingComparisonResponderRiskLevel, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_RESPONDER_RISK_LEVEL_VALUES!r}"
    )
