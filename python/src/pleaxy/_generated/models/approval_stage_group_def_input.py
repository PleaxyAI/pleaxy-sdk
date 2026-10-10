from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_stage_group_def_input_mode import (
    ApprovalStageGroupDefInputMode,
    check_approval_stage_group_def_input_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_stage_def_input import ApprovalStageDefInput
    from ..models.approval_step_condition_input import ApprovalStepConditionInput


T = TypeVar("T", bound="ApprovalStageGroupDefInput")


@_attrs_define
class ApprovalStageGroupDefInput:
    """
    Attributes:
        id (str):
        mode (ApprovalStageGroupDefInputMode):
        stages (List['ApprovalStageDefInput']):
        label (Union[Unset, str]): Human label for the group as a whole, e.g. 'Risk review' - falls back to stage labels
            joined when absent.
        conditions (Union[Unset, List['ApprovalStepConditionInput']]): Include this step only when every condition
            matches the document. Absent or empty = always. The chain must keep at least one step with no conditions.
    """

    id: str
    mode: ApprovalStageGroupDefInputMode
    stages: List["ApprovalStageDefInput"]
    label: Union[Unset, str] = UNSET
    conditions: Union[Unset, List["ApprovalStepConditionInput"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mode: str = self.mode

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        label = self.label

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
                "mode": mode,
                "stages": stages,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_stage_def_input import ApprovalStageDefInput
        from ..models.approval_step_condition_input import ApprovalStepConditionInput

        d = src_dict.copy()
        id = d.pop("id")

        mode = check_approval_stage_group_def_input_mode(d.pop("mode"))

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = ApprovalStageDefInput.from_dict(stages_item_data)

            stages.append(stages_item)

        label = d.pop("label", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ApprovalStepConditionInput.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        approval_stage_group_def_input = cls(
            id=id,
            mode=mode,
            stages=stages,
            label=label,
            conditions=conditions,
        )

        approval_stage_group_def_input.additional_properties = d
        return approval_stage_group_def_input

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
