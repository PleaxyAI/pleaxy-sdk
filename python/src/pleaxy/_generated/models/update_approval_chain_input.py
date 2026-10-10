from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_approval_chain_input_linked_to import (
    UpdateApprovalChainInputLinkedTo,
    check_update_approval_chain_input_linked_to,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_stage_def_input import ApprovalStageDefInput
    from ..models.approval_stage_group_def_input import ApprovalStageGroupDefInput


T = TypeVar("T", bound="UpdateApprovalChainInput")


@_attrs_define
class UpdateApprovalChainInput:
    """
    Attributes:
        use_default (Union[Unset, bool]): Replace the chain with the region's default: one step, 'Region administrator',
            naming the region's owning administrator (or the first administrator by name). Can't be combined with groups,
            stages or linkedTo.
        linked_to (Union[Unset, UpdateApprovalChainInputLinkedTo]): Link this process's chain to another process's
            configured groups, instead of having its own
        stages (Union[Unset, List['ApprovalStageDefInput']]): Legacy flat shape, one sequential stage per step - still
            accepted for backward compatibility. Prefer `groups`; sending this persists as an equivalent single-stage-per-
            group chain. When sent, must have at least one stage - an empty chain would mean zero human approval.
        groups (Union[Unset, List['ApprovalStageGroupDefInput']]): Sequential across groups, parallel (AND-all-required)
            within a group. When sent, must have at least one group - an empty chain would mean zero human approval.
    """

    use_default: Union[Unset, bool] = UNSET
    linked_to: Union[Unset, UpdateApprovalChainInputLinkedTo] = UNSET
    stages: Union[Unset, List["ApprovalStageDefInput"]] = UNSET
    groups: Union[Unset, List["ApprovalStageGroupDefInput"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_default = self.use_default

        linked_to: Union[Unset, str] = UNSET
        if not isinstance(self.linked_to, Unset):
            linked_to = self.linked_to

        stages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_default is not UNSET:
            field_dict["useDefault"] = use_default
        if linked_to is not UNSET:
            field_dict["linkedTo"] = linked_to
        if stages is not UNSET:
            field_dict["stages"] = stages
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_stage_def_input import ApprovalStageDefInput
        from ..models.approval_stage_group_def_input import ApprovalStageGroupDefInput

        d = src_dict.copy()
        use_default = d.pop("useDefault", UNSET)

        _linked_to = d.pop("linkedTo", UNSET)
        linked_to: Union[Unset, UpdateApprovalChainInputLinkedTo]
        if isinstance(_linked_to, Unset):
            linked_to = UNSET
        else:
            linked_to = check_update_approval_chain_input_linked_to(_linked_to)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = ApprovalStageDefInput.from_dict(stages_item_data)

            stages.append(stages_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = ApprovalStageGroupDefInput.from_dict(groups_item_data)

            groups.append(groups_item)

        update_approval_chain_input = cls(
            use_default=use_default,
            linked_to=linked_to,
            stages=stages,
            groups=groups,
        )

        update_approval_chain_input.additional_properties = d
        return update_approval_chain_input

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
