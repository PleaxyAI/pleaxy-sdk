from typing import Literal, Set, cast

CreateApiKeyResultProcurementRole = Literal[
    "administrator",
    "agent",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
]

CREATE_API_KEY_RESULT_PROCUREMENT_ROLE_VALUES: Set[
    CreateApiKeyResultProcurementRole
] = {
    "administrator",
    "agent",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
}


def check_create_api_key_result_procurement_role(
    value: str,
) -> CreateApiKeyResultProcurementRole:
    if value in CREATE_API_KEY_RESULT_PROCUREMENT_ROLE_VALUES:
        return cast(CreateApiKeyResultProcurementRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_RESULT_PROCUREMENT_ROLE_VALUES!r}"
    )
