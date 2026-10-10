from typing import Literal, Set, cast

CloudBulkAccountViewSource = Literal["list", "register"]

CLOUD_BULK_ACCOUNT_VIEW_SOURCE_VALUES: Set[CloudBulkAccountViewSource] = {
    "list",
    "register",
}


def check_cloud_bulk_account_view_source(value: str) -> CloudBulkAccountViewSource:
    if value in CLOUD_BULK_ACCOUNT_VIEW_SOURCE_VALUES:
        return cast(CloudBulkAccountViewSource, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_BULK_ACCOUNT_VIEW_SOURCE_VALUES!r}"
    )
