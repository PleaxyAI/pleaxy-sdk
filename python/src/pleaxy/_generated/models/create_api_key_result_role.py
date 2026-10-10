from typing import Literal, Set, cast

CreateApiKeyResultRole = Literal["buyer", "supplier"]

CREATE_API_KEY_RESULT_ROLE_VALUES: Set[CreateApiKeyResultRole] = {
    "buyer",
    "supplier",
}


def check_create_api_key_result_role(value: str) -> CreateApiKeyResultRole:
    if value in CREATE_API_KEY_RESULT_ROLE_VALUES:
        return cast(CreateApiKeyResultRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_RESULT_ROLE_VALUES!r}"
    )
