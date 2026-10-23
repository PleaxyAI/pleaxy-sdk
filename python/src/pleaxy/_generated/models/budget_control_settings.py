from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.budget_control_settings_mode import (
    BudgetControlSettingsMode,
    check_budget_control_settings_mode,
)
from ..models.budget_control_settings_period import (
    BudgetControlSettingsPeriod,
    check_budget_control_settings_period,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetControlSettings")


@_attrs_define
class BudgetControlSettings:
    """
    Attributes:
        mode (Union[Unset, BudgetControlSettingsMode]):
        period (Union[Unset, BudgetControlSettingsPeriod]):
        updated_at (Union[Unset, str]):
        updated_by (Union[Unset, str]):
    """

    mode: Union[Unset, BudgetControlSettingsMode] = UNSET
    period: Union[Unset, BudgetControlSettingsPeriod] = UNSET
    updated_at: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        period: Union[Unset, str] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period

        updated_at = self.updated_at

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if period is not UNSET:
            field_dict["period"] = period
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, BudgetControlSettingsMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_budget_control_settings_mode(_mode)

        _period = d.pop("period", UNSET)
        period: Union[Unset, BudgetControlSettingsPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = check_budget_control_settings_period(_period)

        updated_at = d.pop("updatedAt", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        budget_control_settings = cls(
            mode=mode,
            period=period,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        budget_control_settings.additional_properties = d
        return budget_control_settings

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
