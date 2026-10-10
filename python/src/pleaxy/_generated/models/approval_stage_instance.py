from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_stage_instance_self_approval_basis import (
    ApprovalStageInstanceSelfApprovalBasis,
    check_approval_stage_instance_self_approval_basis,
)
from ..models.approval_stage_instance_status import (
    ApprovalStageInstanceStatus,
    check_approval_stage_instance_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalStageInstance")


@_attrs_define
class ApprovalStageInstance:
    """
    Attributes:
        id (str):
        label (Union[Unset, str]):
        approver_employee_key (Union[Unset, str]):
        approver_name (Union[Unset, str]):
        status (Union[Unset, ApprovalStageInstanceStatus]):
        self_approval_basis (Union[Unset, ApprovalStageInstanceSelfApprovalBasis]):
    """

    id: str
    label: Union[Unset, str] = UNSET
    approver_employee_key: Union[Unset, str] = UNSET
    approver_name: Union[Unset, str] = UNSET
    status: Union[Unset, ApprovalStageInstanceStatus] = UNSET
    self_approval_basis: Union[Unset, ApprovalStageInstanceSelfApprovalBasis] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        label = self.label

        approver_employee_key = self.approver_employee_key

        approver_name = self.approver_name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        self_approval_basis: Union[Unset, str] = UNSET
        if not isinstance(self.self_approval_basis, Unset):
            self_approval_basis = self.self_approval_basis

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
        if status is not UNSET:
            field_dict["status"] = status
        if self_approval_basis is not UNSET:
            field_dict["selfApprovalBasis"] = self_approval_basis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        label = d.pop("label", UNSET)

        approver_employee_key = d.pop("approverEmployeeKey", UNSET)

        approver_name = d.pop("approverName", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApprovalStageInstanceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_approval_stage_instance_status(_status)

        _self_approval_basis = d.pop("selfApprovalBasis", UNSET)
        self_approval_basis: Union[Unset, ApprovalStageInstanceSelfApprovalBasis]
        if isinstance(_self_approval_basis, Unset):
            self_approval_basis = UNSET
        else:
            self_approval_basis = check_approval_stage_instance_self_approval_basis(
                _self_approval_basis
            )

        approval_stage_instance = cls(
            id=id,
            label=label,
            approver_employee_key=approver_employee_key,
            approver_name=approver_name,
            status=status,
            self_approval_basis=self_approval_basis,
        )

        approval_stage_instance.additional_properties = d
        return approval_stage_instance

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
