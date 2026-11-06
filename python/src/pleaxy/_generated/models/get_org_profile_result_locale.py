from typing import Literal, Set, cast

GetOrgProfileResultLocale = Literal["de", "en", "es", "fr", "it", "pt-BR"]

GET_ORG_PROFILE_RESULT_LOCALE_VALUES: Set[GetOrgProfileResultLocale] = {
    "de",
    "en",
    "es",
    "fr",
    "it",
    "pt-BR",
}


def check_get_org_profile_result_locale(value: str) -> GetOrgProfileResultLocale:
    if value in GET_ORG_PROFILE_RESULT_LOCALE_VALUES:
        return cast(GetOrgProfileResultLocale, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ORG_PROFILE_RESULT_LOCALE_VALUES!r}"
    )
