from typing import Literal, Set, cast

InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1From = Literal[
    "next_month_day"
]

INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_1_FROM_VALUES: Set[
    InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1From
] = {
    "next_month_day",
}


def check_invoice_counterparty_open_purchase_orders_item_default_due_rule_type_1_from(
    value: str,
) -> InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1From:
    if (
        value
        in INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_1_FROM_VALUES
    ):
        return cast(
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType1From, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_1_FROM_VALUES!r}"
    )
