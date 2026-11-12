from typing import Literal, Set, cast

SourcingComparisonStatus = Literal["awarded", "canceled", "closed", "draft", "open"]

SOURCING_COMPARISON_STATUS_VALUES: Set[SourcingComparisonStatus] = {
    "awarded",
    "canceled",
    "closed",
    "draft",
    "open",
}


def check_sourcing_comparison_status(value: str) -> SourcingComparisonStatus:
    if value in SOURCING_COMPARISON_STATUS_VALUES:
        return cast(SourcingComparisonStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_STATUS_VALUES!r}"
    )
