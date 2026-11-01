from typing import Literal, Set, cast

FocusDeliveryTrigger = Literal["manual", "schedule"]

FOCUS_DELIVERY_TRIGGER_VALUES: Set[FocusDeliveryTrigger] = {
    "manual",
    "schedule",
}


def check_focus_delivery_trigger(value: str) -> FocusDeliveryTrigger:
    if value in FOCUS_DELIVERY_TRIGGER_VALUES:
        return cast(FocusDeliveryTrigger, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DELIVERY_TRIGGER_VALUES!r}"
    )
