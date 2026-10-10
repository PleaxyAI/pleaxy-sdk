from typing import Literal, Set, cast

LineItemRuleType = Literal["amount", "quantity"]

LINE_ITEM_RULE_TYPE_VALUES: Set[LineItemRuleType] = {
    "amount",
    "quantity",
}


def check_line_item_rule_type(value: str) -> LineItemRuleType:
    if value in LINE_ITEM_RULE_TYPE_VALUES:
        return cast(LineItemRuleType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LINE_ITEM_RULE_TYPE_VALUES!r}"
    )
