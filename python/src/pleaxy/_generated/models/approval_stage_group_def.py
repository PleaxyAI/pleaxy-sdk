from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_stage_group_def_mode import (
    ApprovalStageGroupDefMode,
    check_approval_stage_group_def_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_stage_def import ApprovalStageDef
    from ..models.approval_step_condition import ApprovalStepCondition


T = TypeVar("T", bound="ApprovalStageGroupDef")


@_attrs_define
class ApprovalStageGroupDef:
    """
    Attributes:
        id (str):
        mode (Union[Unset, ApprovalStageGroupDefMode]):
        label (Union[Unset, str]):
        stages (Union[Unset, List['ApprovalStageDef']]):
        conditions (Union[Unset, List['ApprovalStepCondition']]):
    """

    id: str
    mode: Union[Unset, ApprovalStageGroupDefMode] = UNSET
    label: Union[Unset, str] = UNSET
    stages: Union[Unset, List["ApprovalStageDef"]] = UNSET
    conditions: Union[Unset, List["ApprovalStepCondition"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        label = self.label

        stages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stages, Unset):
            stages = []
            for stages_item_data in self.stages:
                stages_item = stages_item_data.to_dict()
                stages.append(stages_item)

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if label is not UNSET:
            field_dict["label"] = label
        if stages is not UNSET:
            field_dict["stages"] = stages
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_stage_def import ApprovalStageDef
        from ..models.approval_step_condition import ApprovalStepCondition

        d = src_dict.copy()
        id = d.pop("id")

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ApprovalStageGroupDefMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_approval_stage_group_def_mode(_mode)

        label = d.pop("label", UNSET)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = ApprovalStageDef.from_dict(stages_item_data)

            stages.append(stages_item)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ApprovalStepCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        approval_stage_group_def = cls(
            id=id,
            mode=mode,
            label=label,
            stages=stages,
            conditions=conditions,
        )

        approval_stage_group_def.additional_properties = d
        return approval_stage_group_def

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
