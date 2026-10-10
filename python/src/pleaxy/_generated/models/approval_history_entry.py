from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_history_entry_action import (
    ApprovalHistoryEntryAction,
    check_approval_history_entry_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_history_entry_skip import ApprovalHistoryEntrySkip
    from ..models.approval_reassignment_detail import ApprovalReassignmentDetail
    from ..models.self_approval_record import SelfApprovalRecord
    from ..models.spend_limit_history_detail import SpendLimitHistoryDetail


T = TypeVar("T", bound="ApprovalHistoryEntry")


@_attrs_define
class ApprovalHistoryEntry:
    """
    Attributes:
        stage (Union[Unset, str]):
        by (Union[Unset, str]):
        actor_sub (Union[Unset, str]):
        at (Union[Unset, str]):
        action (Union[Unset, ApprovalHistoryEntryAction]):
        detail (Union[Unset, SpendLimitHistoryDetail]):
        reassignment (Union[Unset, ApprovalReassignmentDetail]):
        skip (Union[Unset, ApprovalHistoryEntrySkip]):
        self_approval (Union[Unset, SelfApprovalRecord]):
    """

    stage: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    actor_sub: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    action: Union[Unset, ApprovalHistoryEntryAction] = UNSET
    detail: Union[Unset, "SpendLimitHistoryDetail"] = UNSET
    reassignment: Union[Unset, "ApprovalReassignmentDetail"] = UNSET
    skip: Union[Unset, "ApprovalHistoryEntrySkip"] = UNSET
    self_approval: Union[Unset, "SelfApprovalRecord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stage = self.stage

        by = self.by

        actor_sub = self.actor_sub

        at = self.at

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        reassignment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reassignment, Unset):
            reassignment = self.reassignment.to_dict()

        skip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        self_approval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_approval, Unset):
            self_approval = self.self_approval.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stage is not UNSET:
            field_dict["stage"] = stage
        if by is not UNSET:
            field_dict["by"] = by
        if actor_sub is not UNSET:
            field_dict["actorSub"] = actor_sub
        if at is not UNSET:
            field_dict["at"] = at
        if action is not UNSET:
            field_dict["action"] = action
        if detail is not UNSET:
            field_dict["detail"] = detail
        if reassignment is not UNSET:
            field_dict["reassignment"] = reassignment
        if skip is not UNSET:
            field_dict["skip"] = skip
        if self_approval is not UNSET:
            field_dict["selfApproval"] = self_approval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_history_entry_skip import ApprovalHistoryEntrySkip
        from ..models.approval_reassignment_detail import ApprovalReassignmentDetail
        from ..models.self_approval_record import SelfApprovalRecord
        from ..models.spend_limit_history_detail import SpendLimitHistoryDetail

        d = src_dict.copy()
        stage = d.pop("stage", UNSET)

        by = d.pop("by", UNSET)

        actor_sub = d.pop("actorSub", UNSET)

        at = d.pop("at", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, ApprovalHistoryEntryAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_approval_history_entry_action(_action)

        _detail = d.pop("detail", UNSET)
        detail: Union[Unset, SpendLimitHistoryDetail]
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = SpendLimitHistoryDetail.from_dict(_detail)

        _reassignment = d.pop("reassignment", UNSET)
        reassignment: Union[Unset, ApprovalReassignmentDetail]
        if isinstance(_reassignment, Unset):
            reassignment = UNSET
        else:
            reassignment = ApprovalReassignmentDetail.from_dict(_reassignment)

        _skip = d.pop("skip", UNSET)
        skip: Union[Unset, ApprovalHistoryEntrySkip]
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = ApprovalHistoryEntrySkip.from_dict(_skip)

        _self_approval = d.pop("selfApproval", UNSET)
        self_approval: Union[Unset, SelfApprovalRecord]
        if isinstance(_self_approval, Unset):
            self_approval = UNSET
        else:
            self_approval = SelfApprovalRecord.from_dict(_self_approval)

        approval_history_entry = cls(
            stage=stage,
            by=by,
            actor_sub=actor_sub,
            at=at,
            action=action,
            detail=detail,
            reassignment=reassignment,
            skip=skip,
            self_approval=self_approval,
        )

        approval_history_entry.additional_properties = d
        return approval_history_entry

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
