from typing import Literal, Set, cast

AutomationRuleSetProcess = Literal["invoice_payment", "purchase_order"]

AUTOMATION_RULE_SET_PROCESS_VALUES: Set[AutomationRuleSetProcess] = {
    "invoice_payment",
    "purchase_order",
}


def check_automation_rule_set_process(value: str) -> AutomationRuleSetProcess:
    if value in AUTOMATION_RULE_SET_PROCESS_VALUES:
        return cast(AutomationRuleSetProcess, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUTOMATION_RULE_SET_PROCESS_VALUES!r}"
    )
