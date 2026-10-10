from typing import Literal, Set, cast

GeographyPresetId = Literal[
    "apac",
    "continent-africa",
    "continent-antarctica",
    "continent-asia",
    "continent-europe",
    "continent-north-america",
    "continent-oceania",
    "continent-south-america",
    "eea",
    "emea",
    "eu",
    "global",
    "latam",
    "namer",
    "uk",
]

GEOGRAPHY_PRESET_ID_VALUES: Set[GeographyPresetId] = {
    "apac",
    "continent-africa",
    "continent-antarctica",
    "continent-asia",
    "continent-europe",
    "continent-north-america",
    "continent-oceania",
    "continent-south-america",
    "eea",
    "emea",
    "eu",
    "global",
    "latam",
    "namer",
    "uk",
}


def check_geography_preset_id(value: str) -> GeographyPresetId:
    if value in GEOGRAPHY_PRESET_ID_VALUES:
        return cast(GeographyPresetId, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GEOGRAPHY_PRESET_ID_VALUES!r}"
    )
