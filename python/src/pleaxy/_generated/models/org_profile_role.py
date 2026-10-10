from typing import Literal, Set, cast

OrgProfileRole = Literal["buyer", "supplier"]

ORG_PROFILE_ROLE_VALUES: Set[OrgProfileRole] = {
    "buyer",
    "supplier",
}


def check_org_profile_role(value: str) -> OrgProfileRole:
    if value in ORG_PROFILE_ROLE_VALUES:
        return cast(OrgProfileRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORG_PROFILE_ROLE_VALUES!r}"
    )
