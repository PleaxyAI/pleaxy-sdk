from typing import Literal, Set, cast

CreateCloudConnectionInputProvider = Literal["aws", "azure", "gcp", "oci"]

CREATE_CLOUD_CONNECTION_INPUT_PROVIDER_VALUES: Set[
    CreateCloudConnectionInputProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_create_cloud_connection_input_provider(
    value: str,
) -> CreateCloudConnectionInputProvider:
    if value in CREATE_CLOUD_CONNECTION_INPUT_PROVIDER_VALUES:
        return cast(CreateCloudConnectionInputProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CLOUD_CONNECTION_INPUT_PROVIDER_VALUES!r}"
    )
