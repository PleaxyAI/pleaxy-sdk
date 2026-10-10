from typing import Literal, Set, cast

GetOrgProfileResultRole = Literal["buyer", "supplier"]

GET_ORG_PROFILE_RESULT_ROLE_VALUES: Set[GetOrgProfileResultRole] = {
    "buyer",
    "supplier",
}


def check_get_org_profile_result_role(value: str) -> GetOrgProfileResultRole:
    if value in GET_ORG_PROFILE_RESULT_ROLE_VALUES:
        return cast(GetOrgProfileResultRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ORG_PROFILE_RESULT_ROLE_VALUES!r}"
    )
