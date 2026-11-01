from typing import Literal, Set, cast

FocusDeliveryReason = Literal[
    "accessDenied",
    "assumeRoleFailed",
    "kmsDenied",
    "noSuchBucket",
    "other",
    "wrongRegion",
]

FOCUS_DELIVERY_REASON_VALUES: Set[FocusDeliveryReason] = {
    "accessDenied",
    "assumeRoleFailed",
    "kmsDenied",
    "noSuchBucket",
    "other",
    "wrongRegion",
}


def check_focus_delivery_reason(value: str) -> FocusDeliveryReason:
    if value in FOCUS_DELIVERY_REASON_VALUES:
        return cast(FocusDeliveryReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DELIVERY_REASON_VALUES!r}"
    )
