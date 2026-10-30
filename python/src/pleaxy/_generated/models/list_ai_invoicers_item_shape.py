from typing import Literal, Set, cast

ListAiInvoicersItemShape = Literal["capacity", "credits", "tokens"]

LIST_AI_INVOICERS_ITEM_SHAPE_VALUES: Set[ListAiInvoicersItemShape] = {
    "capacity",
    "credits",
    "tokens",
}


def check_list_ai_invoicers_item_shape(value: str) -> ListAiInvoicersItemShape:
    if value in LIST_AI_INVOICERS_ITEM_SHAPE_VALUES:
        return cast(ListAiInvoicersItemShape, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_SHAPE_VALUES!r}"
    )
