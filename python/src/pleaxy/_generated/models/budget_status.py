from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_status_period import BudgetStatusPeriod


T = TypeVar("T", bound="BudgetStatus")


@_attrs_define
class BudgetStatus:
    """
    Attributes:
        cost_center (Union[Unset, str]):
        cost_center_name (Union[Unset, str]):
        period (Union[Unset, BudgetStatusPeriod]):
        currency (Union[Unset, str]):
        budget (Union[Unset, float]):
        committed (Union[Unset, float]):
        actual (Union[Unset, float]):
        remaining (Union[Unset, float]):
        pending (Union[Unset, float]):
        unconverted (Union[Unset, float]):
    """

    cost_center: Union[Unset, str] = UNSET
    cost_center_name: Union[Unset, str] = UNSET
    period: Union[Unset, "BudgetStatusPeriod"] = UNSET
    currency: Union[Unset, str] = UNSET
    budget: Union[Unset, float] = UNSET
    committed: Union[Unset, float] = UNSET
    actual: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    pending: Union[Unset, float] = UNSET
    unconverted: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        cost_center_name = self.cost_center_name

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        currency = self.currency

        budget = self.budget

        committed = self.committed

        actual = self.actual

        remaining = self.remaining

        pending = self.pending

        unconverted = self.unconverted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if cost_center_name is not UNSET:
            field_dict["costCenterName"] = cost_center_name
        if period is not UNSET:
            field_dict["period"] = period
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
        if pending is not UNSET:
            field_dict["pending"] = pending
        if unconverted is not UNSET:
            field_dict["unconverted"] = unconverted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.budget_status_period import BudgetStatusPeriod

        d = src_dict.copy()
        cost_center = d.pop("costCenter", UNSET)

        cost_center_name = d.pop("costCenterName", UNSET)

        _period = d.pop("period", UNSET)
        period: Union[Unset, BudgetStatusPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = BudgetStatusPeriod.from_dict(_period)

        currency = d.pop("currency", UNSET)

        budget = d.pop("budget", UNSET)

        committed = d.pop("committed", UNSET)

        actual = d.pop("actual", UNSET)

        remaining = d.pop("remaining", UNSET)

        pending = d.pop("pending", UNSET)

        unconverted = d.pop("unconverted", UNSET)

        budget_status = cls(
            cost_center=cost_center,
            cost_center_name=cost_center_name,
            period=period,
            currency=currency,
            budget=budget,
            committed=committed,
            actual=actual,
            remaining=remaining,
            pending=pending,
            unconverted=unconverted,
        )

        budget_status.additional_properties = d
        return budget_status

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
