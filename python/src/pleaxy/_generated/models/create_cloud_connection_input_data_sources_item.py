from typing import Literal, Set, cast

CreateCloudConnectionInputDataSourcesItem = Literal["current_cost", "invoices"]

CREATE_CLOUD_CONNECTION_INPUT_DATA_SOURCES_ITEM_VALUES: Set[
    CreateCloudConnectionInputDataSourcesItem
] = {
    "current_cost",
    "invoices",
}


def check_create_cloud_connection_input_data_sources_item(
    value: str,
) -> CreateCloudConnectionInputDataSourcesItem:
    if value in CREATE_CLOUD_CONNECTION_INPUT_DATA_SOURCES_ITEM_VALUES:
        return cast(CreateCloudConnectionInputDataSourcesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CLOUD_CONNECTION_INPUT_DATA_SOURCES_ITEM_VALUES!r}"
    )
