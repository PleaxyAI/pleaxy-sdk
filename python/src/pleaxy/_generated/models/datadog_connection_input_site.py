from typing import Literal, Set, cast

DatadogConnectionInputSite = Literal[
    "ap1.datadoghq.com",
    "ap2.datadoghq.com",
    "datadoghq.com",
    "datadoghq.eu",
    "ddog-gov.com",
    "uk1.datadoghq.com",
    "us2.ddog-gov.com",
    "us3.datadoghq.com",
    "us5.datadoghq.com",
]

DATADOG_CONNECTION_INPUT_SITE_VALUES: Set[DatadogConnectionInputSite] = {
    "ap1.datadoghq.com",
    "ap2.datadoghq.com",
    "datadoghq.com",
    "datadoghq.eu",
    "ddog-gov.com",
    "uk1.datadoghq.com",
    "us2.ddog-gov.com",
    "us3.datadoghq.com",
    "us5.datadoghq.com",
}


def check_datadog_connection_input_site(value: str) -> DatadogConnectionInputSite:
    if value in DATADOG_CONNECTION_INPUT_SITE_VALUES:
        return cast(DatadogConnectionInputSite, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DATADOG_CONNECTION_INPUT_SITE_VALUES!r}"
    )
