from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_period_kind import BudgetPeriodKind, check_budget_period_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetPeriod")


@_attrs_define
class BudgetPeriod:
    """
    Attributes:
        kind (Union[Unset, BudgetPeriodKind]):
        start (Union[Unset, str]):
        end (Union[Unset, str]):
        fiscal_year (Union[Unset, float]):
    """

    kind: Union[Unset, BudgetPeriodKind] = UNSET
    start: Union[Unset, str] = UNSET
    end: Union[Unset, str] = UNSET
    fiscal_year: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        start = self.start

        end = self.end

        fiscal_year = self.fiscal_year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if fiscal_year is not UNSET:
            field_dict["fiscalYear"] = fiscal_year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, BudgetPeriodKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_budget_period_kind(_kind)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        fiscal_year = d.pop("fiscalYear", UNSET)

        budget_period = cls(
            kind=kind,
            start=start,
            end=end,
            fiscal_year=fiscal_year,
        )

        budget_period.additional_properties = d
        return budget_period

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
