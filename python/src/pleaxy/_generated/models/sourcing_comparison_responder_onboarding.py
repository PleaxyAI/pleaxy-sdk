from typing import Literal, Set, cast

SourcingComparisonResponderOnboarding = Literal[
    "approved", "in_progress", "invited", "pending_invite", "rejected", "submitted"
]

SOURCING_COMPARISON_RESPONDER_ONBOARDING_VALUES: Set[
    SourcingComparisonResponderOnboarding
] = {
    "approved",
    "in_progress",
    "invited",
    "pending_invite",
    "rejected",
    "submitted",
}


def check_sourcing_comparison_responder_onboarding(
    value: str,
) -> SourcingComparisonResponderOnboarding:
    if value in SOURCING_COMPARISON_RESPONDER_ONBOARDING_VALUES:
        return cast(SourcingComparisonResponderOnboarding, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_RESPONDER_ONBOARDING_VALUES!r}"
    )
