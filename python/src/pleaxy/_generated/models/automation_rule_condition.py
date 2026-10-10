from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationRuleCondition")


@_attrs_define
class AutomationRuleCondition:
    """
    Attributes:
        supplier_workspace_id (Union[Unset, str]):
        supplier_contains (Union[Unset, str]):
        max_amount (Union[Unset, float]):
    """

    supplier_workspace_id: Union[Unset, str] = UNSET
    supplier_contains: Union[Unset, str] = UNSET
    max_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_workspace_id = self.supplier_workspace_id

        supplier_contains = self.supplier_contains

        max_amount = self.max_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_workspace_id is not UNSET:
            field_dict["supplierWorkspaceId"] = supplier_workspace_id
        if supplier_contains is not UNSET:
            field_dict["supplierContains"] = supplier_contains
        if max_amount is not UNSET:
            field_dict["maxAmount"] = max_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_workspace_id = d.pop("supplierWorkspaceId", UNSET)

        supplier_contains = d.pop("supplierContains", UNSET)

        max_amount = d.pop("maxAmount", UNSET)

        automation_rule_condition = cls(
            supplier_workspace_id=supplier_workspace_id,
            supplier_contains=supplier_contains,
            max_amount=max_amount,
        )

        automation_rule_condition.additional_properties = d
        return automation_rule_condition

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
