from typing import Literal, Set, cast

RequestTypeDefaultsLineType = Literal["goods", "service"]

REQUEST_TYPE_DEFAULTS_LINE_TYPE_VALUES: Set[RequestTypeDefaultsLineType] = {
    "goods",
    "service",
}


def check_request_type_defaults_line_type(value: str) -> RequestTypeDefaultsLineType:
    if value in REQUEST_TYPE_DEFAULTS_LINE_TYPE_VALUES:
        return cast(RequestTypeDefaultsLineType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REQUEST_TYPE_DEFAULTS_LINE_TYPE_VALUES!r}"
    )
