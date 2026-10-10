from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_chain_settings_linked_to import (
    ApprovalChainSettingsLinkedTo,
    check_approval_chain_settings_linked_to,
)
from ..models.approval_chain_settings_process import (
    ApprovalChainSettingsProcess,
    check_approval_chain_settings_process,
)
from ..models.approval_chain_settings_source import (
    ApprovalChainSettingsSource,
    check_approval_chain_settings_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_chain_settings_requester_rule import (
        ApprovalChainSettingsRequesterRule,
    )
    from ..models.approval_stage_group_def import ApprovalStageGroupDef


T = TypeVar("T", bound="ApprovalChainSettings")


@_attrs_define
class ApprovalChainSettings:
    """
    Attributes:
        process (Union[Unset, ApprovalChainSettingsProcess]):
        linked_to (Union[Unset, ApprovalChainSettingsLinkedTo]):
        groups (Union[Unset, List['ApprovalStageGroupDef']]):
        source (Union[Unset, ApprovalChainSettingsSource]):
        default_approver_is_admin (Union[Unset, bool]):
        requester_rule (Union[Unset, ApprovalChainSettingsRequesterRule]):
    """

    process: Union[Unset, ApprovalChainSettingsProcess] = UNSET
    linked_to: Union[Unset, ApprovalChainSettingsLinkedTo] = UNSET
    groups: Union[Unset, List["ApprovalStageGroupDef"]] = UNSET
    source: Union[Unset, ApprovalChainSettingsSource] = UNSET
    default_approver_is_admin: Union[Unset, bool] = UNSET
    requester_rule: Union[Unset, "ApprovalChainSettingsRequesterRule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process: Union[Unset, str] = UNSET
        if not isinstance(self.process, Unset):
            process = self.process

        linked_to: Union[Unset, str] = UNSET
        if not isinstance(self.linked_to, Unset):
            linked_to = self.linked_to

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        default_approver_is_admin = self.default_approver_is_admin

        requester_rule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.requester_rule, Unset):
            requester_rule = self.requester_rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process is not UNSET:
            field_dict["process"] = process
        if linked_to is not UNSET:
            field_dict["linkedTo"] = linked_to
        if groups is not UNSET:
            field_dict["groups"] = groups
        if source is not UNSET:
            field_dict["source"] = source
        if default_approver_is_admin is not UNSET:
            field_dict["defaultApproverIsAdmin"] = default_approver_is_admin
        if requester_rule is not UNSET:
            field_dict["requesterRule"] = requester_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_chain_settings_requester_rule import (
            ApprovalChainSettingsRequesterRule,
        )
        from ..models.approval_stage_group_def import ApprovalStageGroupDef

        d = src_dict.copy()
        _process = d.pop("process", UNSET)
        process: Union[Unset, ApprovalChainSettingsProcess]
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = check_approval_chain_settings_process(_process)

        _linked_to = d.pop("linkedTo", UNSET)
        linked_to: Union[Unset, ApprovalChainSettingsLinkedTo]
        if isinstance(_linked_to, Unset):
            linked_to = UNSET
        else:
            linked_to = check_approval_chain_settings_linked_to(_linked_to)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ApprovalStageGroupDef.from_dict(groups_item_data)

            groups.append(groups_item)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ApprovalChainSettingsSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_approval_chain_settings_source(_source)

        default_approver_is_admin = d.pop("defaultApproverIsAdmin", UNSET)

        _requester_rule = d.pop("requesterRule", UNSET)
        requester_rule: Union[Unset, ApprovalChainSettingsRequesterRule]
        if isinstance(_requester_rule, Unset):
            requester_rule = UNSET
        else:
            requester_rule = ApprovalChainSettingsRequesterRule.from_dict(
                _requester_rule
            )

        approval_chain_settings = cls(
            process=process,
            linked_to=linked_to,
            groups=groups,
            source=source,
            default_approver_is_admin=default_approver_is_admin,
            requester_rule=requester_rule,
        )

        approval_chain_settings.additional_properties = d
        return approval_chain_settings

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
