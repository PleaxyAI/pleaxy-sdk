from typing import Literal, Set, cast

PunchoutLineOriginKind = Literal["punchout"]

PUNCHOUT_LINE_ORIGIN_KIND_VALUES: Set[PunchoutLineOriginKind] = {
    "punchout",
}


def check_punchout_line_origin_kind(value: str) -> PunchoutLineOriginKind:
    if value in PUNCHOUT_LINE_ORIGIN_KIND_VALUES:
        return cast(PunchoutLineOriginKind, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PUNCHOUT_LINE_ORIGIN_KIND_VALUES!r}"
    )
