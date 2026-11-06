from typing import Literal, Set, cast

UpdateOrgProfileInputLocale = Literal["de", "en", "es", "fr", "it", "pt-BR"]

UPDATE_ORG_PROFILE_INPUT_LOCALE_VALUES: Set[UpdateOrgProfileInputLocale] = {
    "de",
    "en",
    "es",
    "fr",
    "it",
    "pt-BR",
}


def check_update_org_profile_input_locale(value: str) -> UpdateOrgProfileInputLocale:
    if value in UPDATE_ORG_PROFILE_INPUT_LOCALE_VALUES:
        return cast(UpdateOrgProfileInputLocale, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ORG_PROFILE_INPUT_LOCALE_VALUES!r}"
    )
