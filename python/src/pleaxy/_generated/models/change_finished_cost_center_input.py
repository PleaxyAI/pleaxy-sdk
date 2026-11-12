from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChangeFinishedCostCenterInput")


@_attrs_define
class ChangeFinishedCostCenterInput:
    """
    Attributes:
        cost_center (str): The cost center to book the order to: an active one from the workspace's cost centers when it
            keeps a list.
        reason (str): Why it moves, kept on the order with who changed it and when.
    """

    cost_center: str
    reason: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costCenter": cost_center,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center = d.pop("costCenter")

        reason = d.pop("reason")

        change_finished_cost_center_input = cls(
            cost_center=cost_center,
            reason=reason,
        )

        change_finished_cost_center_input.additional_properties = d
        return change_finished_cost_center_input

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
