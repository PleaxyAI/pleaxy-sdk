from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalRoutingSpendLimit")


@_attrs_define
class ApprovalRoutingSpendLimit:
    """
    Attributes:
        employee_key (Union[Unset, str]):
        employee_name (Union[Unset, str]):
        approver_name (Union[Unset, str]):
        satisfied (Union[Unset, bool]):
    """

    employee_key: Union[Unset, str] = UNSET
    employee_name: Union[Unset, str] = UNSET
    approver_name: Union[Unset, str] = UNSET
    satisfied: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employee_key = self.employee_key

        employee_name = self.employee_name

        approver_name = self.approver_name

        satisfied = self.satisfied

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employee_key is not UNSET:
            field_dict["employeeKey"] = employee_key
        if employee_name is not UNSET:
            field_dict["employeeName"] = employee_name
        if approver_name is not UNSET:
            field_dict["approverName"] = approver_name
        if satisfied is not UNSET:
            field_dict["satisfied"] = satisfied

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        employee_key = d.pop("employeeKey", UNSET)

        employee_name = d.pop("employeeName", UNSET)

        approver_name = d.pop("approverName", UNSET)

        satisfied = d.pop("satisfied", UNSET)

        approval_routing_spend_limit = cls(
            employee_key=employee_key,
            employee_name=employee_name,
            approver_name=approver_name,
            satisfied=satisfied,
        )

        approval_routing_spend_limit.additional_properties = d
        return approval_routing_spend_limit

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
