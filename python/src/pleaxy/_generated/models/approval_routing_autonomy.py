from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalRoutingAutonomy")


@_attrs_define
class ApprovalRoutingAutonomy:
    """
    Attributes:
        max_auto_approve_amount (Union[Unset, float]):
        applied (Union[Unset, bool]):
    """

    max_auto_approve_amount: Union[Unset, float] = UNSET
    applied: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_auto_approve_amount = self.max_auto_approve_amount

        applied = self.applied

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_auto_approve_amount is not UNSET:
            field_dict["maxAutoApproveAmount"] = max_auto_approve_amount
        if applied is not UNSET:
            field_dict["applied"] = applied

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_auto_approve_amount = d.pop("maxAutoApproveAmount", UNSET)

        applied = d.pop("applied", UNSET)

        approval_routing_autonomy = cls(
            max_auto_approve_amount=max_auto_approve_amount,
            applied=applied,
        )

        approval_routing_autonomy.additional_properties = d
        return approval_routing_autonomy

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
