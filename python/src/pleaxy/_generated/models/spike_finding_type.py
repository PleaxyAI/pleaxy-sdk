from typing import Literal, Set, cast

SpikeFindingType = Literal["spike"]

SPIKE_FINDING_TYPE_VALUES: Set[SpikeFindingType] = {
    "spike",
}


def check_spike_finding_type(value: str) -> SpikeFindingType:
    if value in SPIKE_FINDING_TYPE_VALUES:
        return cast(SpikeFindingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SPIKE_FINDING_TYPE_VALUES!r}"
    )
