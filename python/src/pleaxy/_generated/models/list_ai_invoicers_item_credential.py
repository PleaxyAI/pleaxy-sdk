from typing import Literal, Set, cast

ListAiInvoicersItemCredential = Literal["admin_key", "key_pair", "none"]

LIST_AI_INVOICERS_ITEM_CREDENTIAL_VALUES: Set[ListAiInvoicersItemCredential] = {
    "admin_key",
    "key_pair",
    "none",
}


def check_list_ai_invoicers_item_credential(
    value: str,
) -> ListAiInvoicersItemCredential:
    if value in LIST_AI_INVOICERS_ITEM_CREDENTIAL_VALUES:
        return cast(ListAiInvoicersItemCredential, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_CREDENTIAL_VALUES!r}"
    )
