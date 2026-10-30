from typing import Literal, Set, cast

ListAiInvoicersItemLegalEntitiesItemRegion = Literal["default", "eu", "us"]

LIST_AI_INVOICERS_ITEM_LEGAL_ENTITIES_ITEM_REGION_VALUES: Set[
    ListAiInvoicersItemLegalEntitiesItemRegion
] = {
    "default",
    "eu",
    "us",
}


def check_list_ai_invoicers_item_legal_entities_item_region(
    value: str,
) -> ListAiInvoicersItemLegalEntitiesItemRegion:
    if value in LIST_AI_INVOICERS_ITEM_LEGAL_ENTITIES_ITEM_REGION_VALUES:
        return cast(ListAiInvoicersItemLegalEntitiesItemRegion, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_LEGAL_ENTITIES_ITEM_REGION_VALUES!r}"
    )
