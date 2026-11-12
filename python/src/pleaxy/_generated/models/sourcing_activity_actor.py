from typing import Literal, Set, cast

SourcingActivityActor = Literal["buyer", "supplier", "system"]

SOURCING_ACTIVITY_ACTOR_VALUES: Set[SourcingActivityActor] = {
    "buyer",
    "supplier",
    "system",
}


def check_sourcing_activity_actor(value: str) -> SourcingActivityActor:
    if value in SOURCING_ACTIVITY_ACTOR_VALUES:
        return cast(SourcingActivityActor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCING_ACTIVITY_ACTOR_VALUES!r}"
    )
