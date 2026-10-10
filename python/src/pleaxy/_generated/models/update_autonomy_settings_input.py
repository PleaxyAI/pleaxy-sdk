from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAutonomySettingsInput")


@_attrs_define
class UpdateAutonomySettingsInput:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        max_auto_approve_amount (Union[Unset, float]):
        approval_threshold (Union[Unset, float]):
    """

    enabled: Union[Unset, bool] = UNSET
    max_auto_approve_amount: Union[Unset, float] = UNSET
    approval_threshold: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        max_auto_approve_amount = self.max_auto_approve_amount

        approval_threshold = self.approval_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_auto_approve_amount is not UNSET:
            field_dict["maxAutoApproveAmount"] = max_auto_approve_amount
        if approval_threshold is not UNSET:
            field_dict["approvalThreshold"] = approval_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        max_auto_approve_amount = d.pop("maxAutoApproveAmount", UNSET)

        approval_threshold = d.pop("approvalThreshold", UNSET)

        update_autonomy_settings_input = cls(
            enabled=enabled,
            max_auto_approve_amount=max_auto_approve_amount,
            approval_threshold=approval_threshold,
        )

        update_autonomy_settings_input.additional_properties = d
        return update_autonomy_settings_input

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
