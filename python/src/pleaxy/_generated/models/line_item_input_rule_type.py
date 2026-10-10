from typing import Literal, Set, cast

LineItemInputRuleType = Literal["amount", "quantity"]

LINE_ITEM_INPUT_RULE_TYPE_VALUES: Set[LineItemInputRuleType] = {
    "amount",
    "quantity",
}


def check_line_item_input_rule_type(value: str) -> LineItemInputRuleType:
    if value in LINE_ITEM_INPUT_RULE_TYPE_VALUES:
        return cast(LineItemInputRuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_INPUT_RULE_TYPE_VALUES!r}"
    )
