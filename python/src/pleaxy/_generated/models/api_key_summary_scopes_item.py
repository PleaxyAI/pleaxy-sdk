from typing import Literal, Set, cast

ApiKeySummaryScopesItem = Literal["invoices:feed"]

API_KEY_SUMMARY_SCOPES_ITEM_VALUES: Set[ApiKeySummaryScopesItem] = {
    "invoices:feed",
}


def check_api_key_summary_scopes_item(value: str) -> ApiKeySummaryScopesItem:
    if value in API_KEY_SUMMARY_SCOPES_ITEM_VALUES:
        return cast(ApiKeySummaryScopesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_KEY_SUMMARY_SCOPES_ITEM_VALUES!r}"
    )
