from typing import Literal, Set, cast

CloudConnectionDataSourcesItem = Literal["current_cost", "invoices"]

CLOUD_CONNECTION_DATA_SOURCES_ITEM_VALUES: Set[CloudConnectionDataSourcesItem] = {
    "current_cost",
    "invoices",
}


def check_cloud_connection_data_sources_item(
    value: str,
) -> CloudConnectionDataSourcesItem:
    if value in CLOUD_CONNECTION_DATA_SOURCES_ITEM_VALUES:
        return cast(CloudConnectionDataSourcesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_DATA_SOURCES_ITEM_VALUES!r}"
    )
