from typing import Literal, Set, cast

FocusDestinationViewDestinationType0Provider = Literal["aws_s3"]

FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_PROVIDER_VALUES: Set[
    FocusDestinationViewDestinationType0Provider
] = {
    "aws_s3",
}


def check_focus_destination_view_destination_type_0_provider(
    value: str,
) -> FocusDestinationViewDestinationType0Provider:
    if value in FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_PROVIDER_VALUES:
        return cast(FocusDestinationViewDestinationType0Provider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FOCUS_DESTINATION_VIEW_DESTINATION_TYPE_0_PROVIDER_VALUES!r}"
    )
