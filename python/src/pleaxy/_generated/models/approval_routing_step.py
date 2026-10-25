from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_step_condition import ApprovalStepCondition


T = TypeVar("T", bound="ApprovalRoutingStep")


@_attrs_define
class ApprovalRoutingStep:
    """
    Attributes:
        step_id (Union[Unset, str]):
        label (Union[Unset, str]):
        applied (Union[Unset, bool]):
        conditions (Union[Unset, List['ApprovalStepCondition']]):
        high_value_only (Union[Unset, bool]):
    """

    step_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    applied: Union[Unset, bool] = UNSET
    conditions: Union[Unset, List["ApprovalStepCondition"]] = UNSET
    high_value_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        step_id = self.step_id

        label = self.label

        applied = self.applied

        conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        high_value_only = self.high_value_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_id is not UNSET:
            field_dict["stepId"] = step_id
        if label is not UNSET:
            field_dict["label"] = label
        if applied is not UNSET:
            field_dict["applied"] = applied
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if high_value_only is not UNSET:
            field_dict["highValueOnly"] = high_value_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.approval_step_condition import ApprovalStepCondition

        d = src_dict.copy()
        step_id = d.pop("stepId", UNSET)

        label = d.pop("label", UNSET)

        applied = d.pop("applied", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ApprovalStepCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        high_value_only = d.pop("highValueOnly", UNSET)

        approval_routing_step = cls(
            step_id=step_id,
            label=label,
            applied=applied,
            conditions=conditions,
            high_value_only=high_value_only,
        )

        approval_routing_step.additional_properties = d
        return approval_routing_step

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
