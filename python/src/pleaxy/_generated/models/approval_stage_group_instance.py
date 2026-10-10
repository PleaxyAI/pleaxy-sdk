from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_stage_group_instance_mode import (
    ApprovalStageGroupInstanceMode,
    check_approval_stage_group_instance_mode,
)
from ..models.approval_stage_group_instance_status import (
    ApprovalStageGroupInstanceStatus,
    check_approval_stage_group_instance_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_stage_instance import ApprovalStageInstance


T = TypeVar("T", bound="ApprovalStageGroupInstance")


@_attrs_define
class ApprovalStageGroupInstance:
    """
    Attributes:
        id (str):
        mode (Union[Unset, ApprovalStageGroupInstanceMode]):
        label (Union[Unset, str]):
        stages (Union[Unset, List['ApprovalStageInstance']]):
        status (Union[Unset, ApprovalStageGroupInstanceStatus]):
    """

    id: str
    mode: Union[Unset, ApprovalStageGroupInstanceMode] = UNSET
    label: Union[Unset, str] = UNSET
    stages: Union[Unset, List["ApprovalStageInstance"]] = UNSET
    status: Union[Unset, ApprovalStageGroupInstanceStatus] = UNSET
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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

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
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_stage_instance import ApprovalStageInstance

        d = src_dict.copy()
        id = d.pop("id")

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ApprovalStageGroupInstanceMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_approval_stage_group_instance_mode(_mode)

        label = d.pop("label", UNSET)

        stages = []
        _stages = d.pop("stages", UNSET)
        for stages_item_data in _stages or []:
            stages_item = ApprovalStageInstance.from_dict(stages_item_data)

            stages.append(stages_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApprovalStageGroupInstanceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_approval_stage_group_instance_status(_status)

        approval_stage_group_instance = cls(
            id=id,
            mode=mode,
            label=label,
            stages=stages,
            status=status,
        )

        approval_stage_group_instance.additional_properties = d
        return approval_stage_group_instance

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
