from typing import Literal, Set, cast

SourcingComparisonFieldType = Literal[
    "date",
    "file",
    "long_text",
    "multi_choice",
    "number",
    "single_choice",
    "text",
    "yes_no",
]

SOURCING_COMPARISON_FIELD_TYPE_VALUES: Set[SourcingComparisonFieldType] = {
    "date",
    "file",
    "long_text",
    "multi_choice",
    "number",
    "single_choice",
    "text",
    "yes_no",
}


def check_sourcing_comparison_field_type(value: str) -> SourcingComparisonFieldType:
    if value in SOURCING_COMPARISON_FIELD_TYPE_VALUES:
        return cast(SourcingComparisonFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_COMPARISON_FIELD_TYPE_VALUES!r}"
    )
