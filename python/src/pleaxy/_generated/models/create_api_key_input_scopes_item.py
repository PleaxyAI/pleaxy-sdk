from typing import Literal, Set, cast

CreateApiKeyInputScopesItem = Literal["invoices:feed"]

CREATE_API_KEY_INPUT_SCOPES_ITEM_VALUES: Set[CreateApiKeyInputScopesItem] = {
    "invoices:feed",
}


def check_create_api_key_input_scopes_item(value: str) -> CreateApiKeyInputScopesItem:
    if value in CREATE_API_KEY_INPUT_SCOPES_ITEM_VALUES:
        return cast(CreateApiKeyInputScopesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_INPUT_SCOPES_ITEM_VALUES!r}"
    )
