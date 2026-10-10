from typing import Literal, Set, cast

RemittanceCheckStatus = Literal["changed", "first", "same"]

REMITTANCE_CHECK_STATUS_VALUES: Set[RemittanceCheckStatus] = {
    "changed",
    "first",
    "same",
}


def check_remittance_check_status(value: str) -> RemittanceCheckStatus:
    if value in REMITTANCE_CHECK_STATUS_VALUES:
        return cast(RemittanceCheckStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMITTANCE_CHECK_STATUS_VALUES!r}"
    )
