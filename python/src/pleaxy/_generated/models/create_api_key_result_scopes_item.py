from typing import Literal, Set, cast

CreateApiKeyResultScopesItem = Literal["invoices:feed"]

CREATE_API_KEY_RESULT_SCOPES_ITEM_VALUES: Set[CreateApiKeyResultScopesItem] = {
    "invoices:feed",
}


def check_create_api_key_result_scopes_item(value: str) -> CreateApiKeyResultScopesItem:
    if value in CREATE_API_KEY_RESULT_SCOPES_ITEM_VALUES:
        return cast(CreateApiKeyResultScopesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_API_KEY_RESULT_SCOPES_ITEM_VALUES!r}"
    )
