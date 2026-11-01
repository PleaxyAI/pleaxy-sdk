from typing import Literal, Set, cast

FocusIssuerViewMappedBy = Literal["name", "person"]

FOCUS_ISSUER_VIEW_MAPPED_BY_VALUES: Set[FocusIssuerViewMappedBy] = {
    "name",
    "person",
}


def check_focus_issuer_view_mapped_by(value: str) -> FocusIssuerViewMappedBy:
    if value in FOCUS_ISSUER_VIEW_MAPPED_BY_VALUES:
        return cast(FocusIssuerViewMappedBy, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_ISSUER_VIEW_MAPPED_BY_VALUES!r}"
    )
