from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_step_condition_input_field import (
    ApprovalStepConditionInputField,
    check_approval_step_condition_input_field,
)
from ..models.approval_step_condition_input_operator import (
    ApprovalStepConditionInputOperator,
    check_approval_step_condition_input_operator,
)

T = TypeVar("T", bound="ApprovalStepConditionInput")


@_attrs_define
class ApprovalStepConditionInput:
    """
    Attributes:
        field (ApprovalStepConditionInputField): The document variable to test.
        operator (ApprovalStepConditionInputOperator): gt/gte/lt/lte for amount; is/is_not for supplier, requester,
            costCenter and glCode.
        value (Union[float, str]): A number for amount (in the region's currency), a supplier Workspace ID for supplier,
            an employee key for requester, a code on the workspace's cost center list for costCenter, a GL account for
            glCode (the order's own, else its cost center's).
    """

    field: ApprovalStepConditionInputField
    operator: ApprovalStepConditionInputOperator
    value: Union[float, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field: str = self.field

        operator: str = self.operator

        value: Union[float, str]
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field": field,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = check_approval_step_condition_input_field(d.pop("field"))

        operator = check_approval_step_condition_input_operator(d.pop("operator"))

        def _parse_value(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        value = _parse_value(d.pop("value"))

        approval_step_condition_input = cls(
            field=field,
            operator=operator,
            value=value,
        )

        approval_step_condition_input.additional_properties = d
        return approval_step_condition_input

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
