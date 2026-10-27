from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_routing_touchless_skipped import (
    ApprovalRoutingTouchlessSkipped,
    check_approval_routing_touchless_skipped,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_routing_autonomy import ApprovalRoutingAutonomy
    from ..models.approval_routing_budget import ApprovalRoutingBudget
    from ..models.approval_routing_rule import ApprovalRoutingRule
    from ..models.approval_routing_spend_limit import ApprovalRoutingSpendLimit
    from ..models.approval_routing_step import ApprovalRoutingStep


T = TypeVar("T", bound="ApprovalRouting")


@_attrs_define
class ApprovalRouting:
    """
    Attributes:
        budget (Union[Unset, ApprovalRoutingBudget]):
        spend_limit (Union[Unset, ApprovalRoutingSpendLimit]):
        rule (Union[Unset, ApprovalRoutingRule]):
        autonomy (Union[Unset, ApprovalRoutingAutonomy]):
        touchless_skipped (Union[Unset, ApprovalRoutingTouchlessSkipped]):
        flagged_answers (Union[Unset, List[str]]):
        steps (Union[Unset, List['ApprovalRoutingStep']]):
    """

    budget: Union[Unset, "ApprovalRoutingBudget"] = UNSET
    spend_limit: Union[Unset, "ApprovalRoutingSpendLimit"] = UNSET
    rule: Union[Unset, "ApprovalRoutingRule"] = UNSET
    autonomy: Union[Unset, "ApprovalRoutingAutonomy"] = UNSET
    touchless_skipped: Union[Unset, ApprovalRoutingTouchlessSkipped] = UNSET
    flagged_answers: Union[Unset, List[str]] = UNSET
    steps: Union[Unset, List["ApprovalRoutingStep"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        budget: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        spend_limit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spend_limit, Unset):
            spend_limit = self.spend_limit.to_dict()

        rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        autonomy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autonomy, Unset):
            autonomy = self.autonomy.to_dict()

        touchless_skipped: Union[Unset, str] = UNSET
        if not isinstance(self.touchless_skipped, Unset):
            touchless_skipped = self.touchless_skipped

        flagged_answers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flagged_answers, Unset):
            flagged_answers = self.flagged_answers

        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget is not UNSET:
            field_dict["budget"] = budget
        if spend_limit is not UNSET:
            field_dict["spendLimit"] = spend_limit
        if rule is not UNSET:
            field_dict["rule"] = rule
        if autonomy is not UNSET:
            field_dict["autonomy"] = autonomy
        if touchless_skipped is not UNSET:
            field_dict["touchlessSkipped"] = touchless_skipped
        if flagged_answers is not UNSET:
            field_dict["flaggedAnswers"] = flagged_answers
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_routing_autonomy import ApprovalRoutingAutonomy
        from ..models.approval_routing_budget import ApprovalRoutingBudget
        from ..models.approval_routing_rule import ApprovalRoutingRule
        from ..models.approval_routing_spend_limit import ApprovalRoutingSpendLimit
        from ..models.approval_routing_step import ApprovalRoutingStep

        d = src_dict.copy()
        _budget = d.pop("budget", UNSET)
        budget: Union[Unset, ApprovalRoutingBudget]
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = ApprovalRoutingBudget.from_dict(_budget)

        _spend_limit = d.pop("spendLimit", UNSET)
        spend_limit: Union[Unset, ApprovalRoutingSpendLimit]
        if isinstance(_spend_limit, Unset):
            spend_limit = UNSET
        else:
            spend_limit = ApprovalRoutingSpendLimit.from_dict(_spend_limit)

        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, ApprovalRoutingRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = ApprovalRoutingRule.from_dict(_rule)

        _autonomy = d.pop("autonomy", UNSET)
        autonomy: Union[Unset, ApprovalRoutingAutonomy]
        if isinstance(_autonomy, Unset):
            autonomy = UNSET
        else:
            autonomy = ApprovalRoutingAutonomy.from_dict(_autonomy)

        _touchless_skipped = d.pop("touchlessSkipped", UNSET)
        touchless_skipped: Union[Unset, ApprovalRoutingTouchlessSkipped]
        if isinstance(_touchless_skipped, Unset):
            touchless_skipped = UNSET
        else:
            touchless_skipped = check_approval_routing_touchless_skipped(
                _touchless_skipped
            )

        flagged_answers = cast(List[str], d.pop("flaggedAnswers", UNSET))

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = ApprovalRoutingStep.from_dict(steps_item_data)

            steps.append(steps_item)

        approval_routing = cls(
            budget=budget,
            spend_limit=spend_limit,
            rule=rule,
            autonomy=autonomy,
            touchless_skipped=touchless_skipped,
            flagged_answers=flagged_answers,
            steps=steps,
        )

        approval_routing.additional_properties = d
        return approval_routing

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
