from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_budget_control_input_mode import (
    UpdateBudgetControlInputMode,
    check_update_budget_control_input_mode,
)
from ..models.update_budget_control_input_period import (
    UpdateBudgetControlInputPeriod,
    check_update_budget_control_input_period,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBudgetControlInput")


@_attrs_define
class UpdateBudgetControlInput:
    """
    Attributes:
        mode (Union[Unset, UpdateBudgetControlInputMode]): off: no check. warn: an order over budget goes ahead, never
            auto-approved, with a warning. block: it is refused.
        period (Union[Unset, UpdateBudgetControlInputPeriod]): The budget period a check uses: the fiscal month, quarter
            or year containing the day it runs.
    """

    mode: Union[Unset, UpdateBudgetControlInputMode] = UNSET
    period: Union[Unset, UpdateBudgetControlInputPeriod] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        period: Union[Unset, str] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, UpdateBudgetControlInputMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_update_budget_control_input_mode(_mode)

        _period = d.pop("period", UNSET)
        period: Union[Unset, UpdateBudgetControlInputPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = check_update_budget_control_input_period(_period)

        update_budget_control_input = cls(
            mode=mode,
            period=period,
        )

        update_budget_control_input.additional_properties = d
        return update_budget_control_input

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
