from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_routing_budget_mode import (
    ApprovalRoutingBudgetMode,
    check_approval_routing_budget_mode,
)
from ..models.approval_routing_budget_outcome import (
    ApprovalRoutingBudgetOutcome,
    check_approval_routing_budget_outcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_routing_budget_period import ApprovalRoutingBudgetPeriod


T = TypeVar("T", bound="ApprovalRoutingBudget")


@_attrs_define
class ApprovalRoutingBudget:
    """
    Attributes:
        outcome (Union[Unset, ApprovalRoutingBudgetOutcome]):
        mode (Union[Unset, ApprovalRoutingBudgetMode]):
        cost_center (Union[Unset, str]):
        period (Union[Unset, ApprovalRoutingBudgetPeriod]):
        currency (Union[Unset, str]):
        over_by (Union[Unset, float]):
    """

    outcome: Union[Unset, ApprovalRoutingBudgetOutcome] = UNSET
    mode: Union[Unset, ApprovalRoutingBudgetMode] = UNSET
    cost_center: Union[Unset, str] = UNSET
    period: Union[Unset, "ApprovalRoutingBudgetPeriod"] = UNSET
    currency: Union[Unset, str] = UNSET
    over_by: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        cost_center = self.cost_center

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        currency = self.currency

        over_by = self.over_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if mode is not UNSET:
            field_dict["mode"] = mode
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if period is not UNSET:
            field_dict["period"] = period
        if currency is not UNSET:
            field_dict["currency"] = currency
        if over_by is not UNSET:
            field_dict["overBy"] = over_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_routing_budget_period import ApprovalRoutingBudgetPeriod

        d = src_dict.copy()
        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, ApprovalRoutingBudgetOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_approval_routing_budget_outcome(_outcome)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ApprovalRoutingBudgetMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_approval_routing_budget_mode(_mode)

        cost_center = d.pop("costCenter", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, ApprovalRoutingBudgetPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = ApprovalRoutingBudgetPeriod.from_dict(_period)

        currency = d.pop("currency", UNSET)

        over_by = d.pop("overBy", UNSET)

        approval_routing_budget = cls(
            outcome=outcome,
            mode=mode,
            cost_center=cost_center,
            period=period,
            currency=currency,
            over_by=over_by,
        )

        approval_routing_budget.additional_properties = d
        return approval_routing_budget

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
