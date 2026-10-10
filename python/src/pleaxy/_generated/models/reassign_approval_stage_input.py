from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReassignApprovalStageInput")


@_attrs_define
class ReassignApprovalStageInput:
    """
    Attributes:
        stage_id (str): Id of the pending stage to reassign. May be in any group, not only the current one.
        approver_employee_key (str): Employee key (Cognito sub) of the new approver. Must be a buyer member of this
            workspace, and not the acting administrator.
        reason (Union[Unset, str]): Why the step was reassigned - shown in the approval history.
    """

    stage_id: str
    approver_employee_key: str
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stage_id = self.stage_id

        approver_employee_key = self.approver_employee_key

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stageId": stage_id,
                "approverEmployeeKey": approver_employee_key,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stage_id = d.pop("stageId")

        approver_employee_key = d.pop("approverEmployeeKey")

        reason = d.pop("reason", UNSET)

        reassign_approval_stage_input = cls(
            stage_id=stage_id,
            approver_employee_key=approver_employee_key,
            reason=reason,
        )

        reassign_approval_stage_input.additional_properties = d
        return reassign_approval_stage_input

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
