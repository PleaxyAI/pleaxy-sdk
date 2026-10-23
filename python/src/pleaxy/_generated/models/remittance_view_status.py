from typing import Literal, Set, cast

RemittanceViewStatus = Literal[
    "paid_through_pleaxy", "processing", "recorded", "unpaid", "withdrawn"
]

REMITTANCE_VIEW_STATUS_VALUES: Set[RemittanceViewStatus] = {
    "paid_through_pleaxy",
    "processing",
    "recorded",
    "unpaid",
    "withdrawn",
}


def check_remittance_view_status(value: str) -> RemittanceViewStatus:
    if value in REMITTANCE_VIEW_STATUS_VALUES:
        return cast(RemittanceViewStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_VIEW_STATUS_VALUES!r}"
    )
