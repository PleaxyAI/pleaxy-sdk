from typing import Literal, Set, cast

GetFocusSourcePeriodResultVersion = Literal["1.0", "1.1", "1.2", "1.3", "1.4"]

GET_FOCUS_SOURCE_PERIOD_RESULT_VERSION_VALUES: Set[
    GetFocusSourcePeriodResultVersion
] = {
    "1.0",
    "1.1",
    "1.2",
    "1.3",
    "1.4",
}


def check_get_focus_source_period_result_version(
    value: str,
) -> GetFocusSourcePeriodResultVersion:
    if value in GET_FOCUS_SOURCE_PERIOD_RESULT_VERSION_VALUES:
        return cast(GetFocusSourcePeriodResultVersion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_FOCUS_SOURCE_PERIOD_RESULT_VERSION_VALUES!r}"
    )
