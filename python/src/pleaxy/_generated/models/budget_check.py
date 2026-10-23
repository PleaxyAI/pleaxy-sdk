from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_check_mode import BudgetCheckMode, check_budget_check_mode
from ..models.budget_check_outcome import BudgetCheckOutcome, check_budget_check_outcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_check_period import BudgetCheckPeriod


T = TypeVar("T", bound="BudgetCheck")


@_attrs_define
class BudgetCheck:
    """
    Attributes:
        outcome (Union[Unset, BudgetCheckOutcome]):
        mode (Union[Unset, BudgetCheckMode]):
        period (Union[Unset, BudgetCheckPeriod]):
        cost_center (Union[Unset, str]):
        currency (Union[Unset, str]):
        budget (Union[Unset, float]):
        committed (Union[Unset, float]):
        actual (Union[Unset, float]):
        remaining (Union[Unset, float]):
        amount (Union[Unset, float]):
        over_by (Union[Unset, float]):
        checked_at (Union[Unset, str]):
    """

    outcome: Union[Unset, BudgetCheckOutcome] = UNSET
    mode: Union[Unset, BudgetCheckMode] = UNSET
    period: Union[Unset, "BudgetCheckPeriod"] = UNSET
    cost_center: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    budget: Union[Unset, float] = UNSET
    committed: Union[Unset, float] = UNSET
    actual: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET
    over_by: Union[Unset, float] = UNSET
    checked_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        cost_center = self.cost_center

        currency = self.currency

        budget = self.budget

        committed = self.committed

        actual = self.actual

        remaining = self.remaining

        amount = self.amount

        over_by = self.over_by

        checked_at = self.checked_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if mode is not UNSET:
            field_dict["mode"] = mode
        if period is not UNSET:
            field_dict["period"] = period
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if currency is not UNSET:
            field_dict["currency"] = currency
        if budget is not UNSET:
            field_dict["budget"] = budget
        if committed is not UNSET:
            field_dict["committed"] = committed
        if actual is not UNSET:
            field_dict["actual"] = actual
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if amount is not UNSET:
            field_dict["amount"] = amount
        if over_by is not UNSET:
            field_dict["overBy"] = over_by
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.budget_check_period import BudgetCheckPeriod

        d = src_dict.copy()
        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, BudgetCheckOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_budget_check_outcome(_outcome)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BudgetCheckMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_budget_check_mode(_mode)

        _period = d.pop("period", UNSET)
        period: Union[Unset, BudgetCheckPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = BudgetCheckPeriod.from_dict(_period)

        cost_center = d.pop("costCenter", UNSET)

        currency = d.pop("currency", UNSET)

        budget = d.pop("budget", UNSET)

        committed = d.pop("committed", UNSET)

        actual = d.pop("actual", UNSET)

        remaining = d.pop("remaining", UNSET)

        amount = d.pop("amount", UNSET)

        over_by = d.pop("overBy", UNSET)

        checked_at = d.pop("checkedAt", UNSET)

        budget_check = cls(
            outcome=outcome,
            mode=mode,
            period=period,
            cost_center=cost_center,
            currency=currency,
            budget=budget,
            committed=committed,
            actual=actual,
            remaining=remaining,
            amount=amount,
            over_by=over_by,
            checked_at=checked_at,
        )

        budget_check.additional_properties = d
        return budget_check

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
