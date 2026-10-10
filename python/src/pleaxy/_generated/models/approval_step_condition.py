from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_step_condition_field import (
    ApprovalStepConditionField,
    check_approval_step_condition_field,
)
from ..models.approval_step_condition_operator import (
    ApprovalStepConditionOperator,
    check_approval_step_condition_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalStepCondition")


@_attrs_define
class ApprovalStepCondition:
    """
    Attributes:
        field (Union[Unset, ApprovalStepConditionField]):
        operator (Union[Unset, ApprovalStepConditionOperator]):
        value (Union[Unset, float, str]):
    """

    field: Union[Unset, ApprovalStepConditionField] = UNSET
    operator: Union[Unset, ApprovalStepConditionOperator] = UNSET
    value: Union[Unset, float, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: Union[Unset, str] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator

        value: Union[Unset, float, str]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _field = d.pop("field", UNSET)
        field: Union[Unset, ApprovalStepConditionField]
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = check_approval_step_condition_field(_field)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, ApprovalStepConditionOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = check_approval_step_condition_operator(_operator)

        def _parse_value(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        value = _parse_value(d.pop("value", UNSET))

        approval_step_condition = cls(
            field=field,
            operator=operator,
            value=value,
        )

        approval_step_condition.additional_properties = d
        return approval_step_condition

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
