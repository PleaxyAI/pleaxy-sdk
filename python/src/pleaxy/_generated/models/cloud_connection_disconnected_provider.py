from typing import Literal, Set, cast

CloudConnectionDisconnectedProvider = Literal["aws", "azure", "gcp", "oci"]

CLOUD_CONNECTION_DISCONNECTED_PROVIDER_VALUES: Set[
    CloudConnectionDisconnectedProvider
] = {
    "aws",
    "azure",
    "gcp",
    "oci",
}


def check_cloud_connection_disconnected_provider(
    value: str,
) -> CloudConnectionDisconnectedProvider:
    if value in CLOUD_CONNECTION_DISCONNECTED_PROVIDER_VALUES:
        return cast(CloudConnectionDisconnectedProvider, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_DISCONNECTED_PROVIDER_VALUES!r}"
    )
