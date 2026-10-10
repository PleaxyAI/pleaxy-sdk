from typing import Literal, Set, cast

AutomationRuleSetViewProcess = Literal["invoice_payment", "purchase_order"]

AUTOMATION_RULE_SET_VIEW_PROCESS_VALUES: Set[AutomationRuleSetViewProcess] = {
    "invoice_payment",
    "purchase_order",
}


def check_automation_rule_set_view_process(value: str) -> AutomationRuleSetViewProcess:
    if value in AUTOMATION_RULE_SET_VIEW_PROCESS_VALUES:
        return cast(AutomationRuleSetViewProcess, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTOMATION_RULE_SET_VIEW_PROCESS_VALUES!r}"
    )
