from typing import Literal, Set, cast

OrgProfileLocale = Literal["de", "en", "es", "fr", "it", "pt-BR"]

ORG_PROFILE_LOCALE_VALUES: Set[OrgProfileLocale] = {
    "de",
    "en",
    "es",
    "fr",
    "it",
    "pt-BR",
}


def check_org_profile_locale(value: str) -> OrgProfileLocale:
    if value in ORG_PROFILE_LOCALE_VALUES:
        return cast(OrgProfileLocale, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORG_PROFILE_LOCALE_VALUES!r}"
    )
