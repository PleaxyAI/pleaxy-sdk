from typing import Literal, Set, cast

CreateApiKeyInputProcurementRole = Literal[
    "administrator",
    "agent",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
]

CREATE_API_KEY_INPUT_PROCUREMENT_ROLE_VALUES: Set[CreateApiKeyInputProcurementRole] = {
    "administrator",
    "agent",
    "contracts-and-suppliers",
    "finance",
    "read-only",
    "relationships",
    "requisitions",
}


def check_create_api_key_input_procurement_role(
    value: str,
) -> CreateApiKeyInputProcurementRole:
    if value in CREATE_API_KEY_INPUT_PROCUREMENT_ROLE_VALUES:
        return cast(CreateApiKeyInputProcurementRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_INPUT_PROCUREMENT_ROLE_VALUES!r}"
    )
