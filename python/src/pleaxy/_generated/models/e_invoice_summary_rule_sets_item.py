from typing import Literal, Set, cast

EInvoiceSummaryRuleSetsItem = Literal["en16931", "xrechnung"]

E_INVOICE_SUMMARY_RULE_SETS_ITEM_VALUES: Set[EInvoiceSummaryRuleSetsItem] = {
    "en16931",
    "xrechnung",
}


def check_e_invoice_summary_rule_sets_item(value: str) -> EInvoiceSummaryRuleSetsItem:
    if value in E_INVOICE_SUMMARY_RULE_SETS_ITEM_VALUES:
        return cast(EInvoiceSummaryRuleSetsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {E_INVOICE_SUMMARY_RULE_SETS_ITEM_VALUES!r}"
    )
