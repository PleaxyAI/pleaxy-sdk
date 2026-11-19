from typing import Literal, Set, cast

InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From = Literal[
    "end_of_month"
]

INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_0_FROM_VALUES: Set[
    InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From
] = {
    "end_of_month",
}


def check_invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0_from(
    value: str,
) -> InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From:
    if (
        value
        in INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_0_FROM_VALUES
    ):
        return cast(
            InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From, value
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INVOICE_COUNTERPARTY_OPEN_PURCHASE_ORDERS_ITEM_DEFAULT_DUE_RULE_TYPE_0_FROM_VALUES!r}"
    )
