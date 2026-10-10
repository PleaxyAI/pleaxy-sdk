from typing import Literal, Set, cast

UpdateOrgProfileInputGeographyPresetId = Literal[
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

UPDATE_ORG_PROFILE_INPUT_GEOGRAPHY_PRESET_ID_VALUES: Set[
    UpdateOrgProfileInputGeographyPresetId
] = {
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


def check_update_org_profile_input_geography_preset_id(
    value: str,
) -> UpdateOrgProfileInputGeographyPresetId:
    if value in UPDATE_ORG_PROFILE_INPUT_GEOGRAPHY_PRESET_ID_VALUES:
        return cast(UpdateOrgProfileInputGeographyPresetId, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ORG_PROFILE_INPUT_GEOGRAPHY_PRESET_ID_VALUES!r}"
    )
