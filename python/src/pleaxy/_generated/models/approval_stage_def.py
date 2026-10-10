from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalStageDef")


@_attrs_define
class ApprovalStageDef:
    """
    Attributes:
        id (str):
        label (Union[Unset, str]):
        approver_employee_key (Union[Unset, str]):
        approver_name (Union[Unset, str]):
        approver_email (Union[Unset, str]):
        high_value_only (Union[Unset, bool]):
    """

    id: str
    label: Union[Unset, str] = UNSET
    approver_employee_key: Union[Unset, str] = UNSET
    approver_name: Union[Unset, str] = UNSET
    approver_email: Union[Unset, str] = UNSET
    high_value_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        approver_employee_key = self.approver_employee_key

        approver_name = self.approver_name

        approver_email = self.approver_email

        high_value_only = self.high_value_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if approver_employee_key is not UNSET:
            field_dict["approverEmployeeKey"] = approver_employee_key
        if approver_name is not UNSET:
            field_dict["approverName"] = approver_name
        if approver_email is not UNSET:
            field_dict["approverEmail"] = approver_email
        if high_value_only is not UNSET:
            field_dict["highValueOnly"] = high_value_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label", UNSET)

        approver_employee_key = d.pop("approverEmployeeKey", UNSET)

        approver_name = d.pop("approverName", UNSET)

        approver_email = d.pop("approverEmail", UNSET)

        high_value_only = d.pop("highValueOnly", UNSET)

        approval_stage_def = cls(
            id=id,
            label=label,
            approver_employee_key=approver_employee_key,
            approver_name=approver_name,
            approver_email=approver_email,
            high_value_only=high_value_only,
        )

        approval_stage_def.additional_properties = d
        return approval_stage_def

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
