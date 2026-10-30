from typing import Literal, Set, cast

ListAiInvoicersItemBillingItem = Literal["invoice", "prepaid_credits"]

LIST_AI_INVOICERS_ITEM_BILLING_ITEM_VALUES: Set[ListAiInvoicersItemBillingItem] = {
    "invoice",
    "prepaid_credits",
}


def check_list_ai_invoicers_item_billing_item(
    value: str,
) -> ListAiInvoicersItemBillingItem:
    if value in LIST_AI_INVOICERS_ITEM_BILLING_ITEM_VALUES:
        return cast(ListAiInvoicersItemBillingItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AI_INVOICERS_ITEM_BILLING_ITEM_VALUES!r}"
    )
