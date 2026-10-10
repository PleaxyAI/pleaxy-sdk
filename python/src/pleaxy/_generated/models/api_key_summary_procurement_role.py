from typing import Literal, Set, cast

ApiKeySummaryProcurementRole = Literal[
    "administrator",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
]

API_KEY_SUMMARY_PROCUREMENT_ROLE_VALUES: Set[ApiKeySummaryProcurementRole] = {
    "administrator",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
}


def check_api_key_summary_procurement_role(value: str) -> ApiKeySummaryProcurementRole:
    if value in API_KEY_SUMMARY_PROCUREMENT_ROLE_VALUES:
        return cast(ApiKeySummaryProcurementRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_KEY_SUMMARY_PROCUREMENT_ROLE_VALUES!r}"
    )
