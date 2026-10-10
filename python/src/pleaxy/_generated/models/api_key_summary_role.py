from typing import Literal, Set, cast

ApiKeySummaryRole = Literal["buyer", "supplier"]

API_KEY_SUMMARY_ROLE_VALUES: Set[ApiKeySummaryRole] = {
    "buyer",
    "supplier",
}


def check_api_key_summary_role(value: str) -> ApiKeySummaryRole:
    if value in API_KEY_SUMMARY_ROLE_VALUES:
        return cast(ApiKeySummaryRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_KEY_SUMMARY_ROLE_VALUES!r}"
    )
