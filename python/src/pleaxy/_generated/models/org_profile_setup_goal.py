from typing import Literal, Set, cast

OrgProfileSetupGoal = Literal["audit", "network"]

ORG_PROFILE_SETUP_GOAL_VALUES: Set[OrgProfileSetupGoal] = {
    "audit",
    "network",
}


def check_org_profile_setup_goal(value: str) -> OrgProfileSetupGoal:
    if value in ORG_PROFILE_SETUP_GOAL_VALUES:
        return cast(OrgProfileSetupGoal, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORG_PROFILE_SETUP_GOAL_VALUES!r}"
    )
