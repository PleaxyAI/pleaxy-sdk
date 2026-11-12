from typing import Literal, Set, cast

GetOrgProfileResultSetupGoal = Literal["audit", "network"]

GET_ORG_PROFILE_RESULT_SETUP_GOAL_VALUES: Set[GetOrgProfileResultSetupGoal] = {
    "audit",
    "network",
}


def check_get_org_profile_result_setup_goal(value: str) -> GetOrgProfileResultSetupGoal:
    if value in GET_ORG_PROFILE_RESULT_SETUP_GOAL_VALUES:
        return cast(GetOrgProfileResultSetupGoal, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ORG_PROFILE_RESULT_SETUP_GOAL_VALUES!r}"
    )
