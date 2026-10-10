from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalStageDefInput")


@_attrs_define
class ApprovalStageDefInput:
    """
    Attributes:
        id (str):
        label (str):
        approver_employee_key (str): Employee key (Cognito sub) of the approver. Required and non-empty: a step is
            actionable only by the employee it names. There is no 'unassigned' step.
        high_value_only (Union[Unset, bool]):
    """

    id: str
    label: str
    approver_employee_key: str
    high_value_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        approver_employee_key = self.approver_employee_key

        high_value_only = self.high_value_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "approverEmployeeKey": approver_employee_key,
            }
        )
        if high_value_only is not UNSET:
            field_dict["highValueOnly"] = high_value_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label")

        approver_employee_key = d.pop("approverEmployeeKey")

        high_value_only = d.pop("highValueOnly", UNSET)

        approval_stage_def_input = cls(
            id=id,
            label=label,
            approver_employee_key=approver_employee_key,
            high_value_only=high_value_only,
        )

        approval_stage_def_input.additional_properties = d
        return approval_stage_def_input

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
