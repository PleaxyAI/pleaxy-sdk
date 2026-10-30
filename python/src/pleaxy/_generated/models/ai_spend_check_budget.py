from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSpendCheckBudget")


@_attrs_define
class AiSpendCheckBudget:
    """
    Attributes:
        cost_center (Union[Unset, str]):
        budget (Union[Unset, float]):
        committed (Union[Unset, float]):
        actual (Union[Unset, float]):
        accruing (Union[Unset, float]):
        remaining (Union[Unset, float]):
    """

    cost_center: Union[Unset, str] = UNSET
    budget: Union[Unset, float] = UNSET
    committed: Union[Unset, float] = UNSET
    actual: Union[Unset, float] = UNSET
    accruing: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        budget = self.budget

        committed = self.committed

        actual = self.actual

        accruing = self.accruing

        remaining = self.remaining

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if budget is not UNSET:
            field_dict["budget"] = budget
        if committed is not UNSET:
            field_dict["committed"] = committed
        if actual is not UNSET:
            field_dict["actual"] = actual
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if remaining is not UNSET:
            field_dict["remaining"] = remaining

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center = d.pop("costCenter", UNSET)

        budget = d.pop("budget", UNSET)

        committed = d.pop("committed", UNSET)

        actual = d.pop("actual", UNSET)

        accruing = d.pop("accruing", UNSET)

        remaining = d.pop("remaining", UNSET)

        ai_spend_check_budget = cls(
            cost_center=cost_center,
            budget=budget,
            committed=committed,
            actual=actual,
            accruing=accruing,
            remaining=remaining,
        )

        ai_spend_check_budget.additional_properties = d
        return ai_spend_check_budget

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
