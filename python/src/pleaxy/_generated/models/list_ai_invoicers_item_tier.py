from typing import Literal, Set, cast

ListAiInvoicersItemTier = Literal[
    "data_platform", "direct", "host", "neocloud", "seats"
]

LIST_AI_INVOICERS_ITEM_TIER_VALUES: Set[ListAiInvoicersItemTier] = {
    "data_platform",
    "direct",
    "host",
    "neocloud",
    "seats",
}


def check_list_ai_invoicers_item_tier(value: str) -> ListAiInvoicersItemTier:
    if value in LIST_AI_INVOICERS_ITEM_TIER_VALUES:
        return cast(ListAiInvoicersItemTier, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_TIER_VALUES!r}"
    )
