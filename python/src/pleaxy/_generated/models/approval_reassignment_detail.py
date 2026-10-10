from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_reassignment_detail_by_policy import (
    ApprovalReassignmentDetailByPolicy,
    check_approval_reassignment_detail_by_policy,
)
from ..models.approval_reassignment_detail_on_rebuild import (
    ApprovalReassignmentDetailOnRebuild,
    check_approval_reassignment_detail_on_rebuild,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalReassignmentDetail")


@_attrs_define
class ApprovalReassignmentDetail:
    """
    Attributes:
        from_employee_key (Union[Unset, str]):
        from_name (Union[Unset, str]):
        to_employee_key (Union[Unset, str]):
        to_name (Union[Unset, str]):
        reason (Union[Unset, str]):
        on_rebuild (Union[Unset, ApprovalReassignmentDetailOnRebuild]):
        by_policy (Union[Unset, ApprovalReassignmentDetailByPolicy]):
    """

    from_employee_key: Union[Unset, str] = UNSET
    from_name: Union[Unset, str] = UNSET
    to_employee_key: Union[Unset, str] = UNSET
    to_name: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    on_rebuild: Union[Unset, ApprovalReassignmentDetailOnRebuild] = UNSET
    by_policy: Union[Unset, ApprovalReassignmentDetailByPolicy] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_employee_key = self.from_employee_key

        from_name = self.from_name

        to_employee_key = self.to_employee_key

        to_name = self.to_name

        reason = self.reason

        on_rebuild: Union[Unset, str] = UNSET
        if not isinstance(self.on_rebuild, Unset):
            on_rebuild = self.on_rebuild

        by_policy: Union[Unset, str] = UNSET
        if not isinstance(self.by_policy, Unset):
            by_policy = self.by_policy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_employee_key is not UNSET:
            field_dict["fromEmployeeKey"] = from_employee_key
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if to_employee_key is not UNSET:
            field_dict["toEmployeeKey"] = to_employee_key
        if to_name is not UNSET:
            field_dict["toName"] = to_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if on_rebuild is not UNSET:
            field_dict["onRebuild"] = on_rebuild
        if by_policy is not UNSET:
            field_dict["byPolicy"] = by_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_employee_key = d.pop("fromEmployeeKey", UNSET)

        from_name = d.pop("fromName", UNSET)

        to_employee_key = d.pop("toEmployeeKey", UNSET)

        to_name = d.pop("toName", UNSET)

        reason = d.pop("reason", UNSET)

        _on_rebuild = d.pop("onRebuild", UNSET)
        on_rebuild: Union[Unset, ApprovalReassignmentDetailOnRebuild]
        if isinstance(_on_rebuild, Unset):
            on_rebuild = UNSET
        else:
            on_rebuild = check_approval_reassignment_detail_on_rebuild(_on_rebuild)

        _by_policy = d.pop("byPolicy", UNSET)
        by_policy: Union[Unset, ApprovalReassignmentDetailByPolicy]
        if isinstance(_by_policy, Unset):
            by_policy = UNSET
        else:
            by_policy = check_approval_reassignment_detail_by_policy(_by_policy)

        approval_reassignment_detail = cls(
            from_employee_key=from_employee_key,
            from_name=from_name,
            to_employee_key=to_employee_key,
            to_name=to_name,
            reason=reason,
            on_rebuild=on_rebuild,
            by_policy=by_policy,
        )

        approval_reassignment_detail.additional_properties = d
        return approval_reassignment_detail

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
