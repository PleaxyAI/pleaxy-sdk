from typing import Literal, Set, cast

CloudConnectionProvider = Literal["aws", "azure", "gcp", "oci"]

CLOUD_CONNECTION_PROVIDER_VALUES: Set[CloudConnectionProvider] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_cloud_connection_provider(value: str) -> CloudConnectionProvider:
    if value in CLOUD_CONNECTION_PROVIDER_VALUES:
        return cast(CloudConnectionProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_PROVIDER_VALUES!r}"
    )
