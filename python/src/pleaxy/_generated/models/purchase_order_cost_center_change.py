from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderCostCenterChange")


@_attrs_define
class PurchaseOrderCostCenterChange:
    """
    Attributes:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        reason (Union[Unset, str]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        at (Union[Unset, str]):
    """

    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        reason = self.reason

        by = self.by

        by_name = self.by_name

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if reason is not UNSET:
            field_dict["reason"] = reason
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        reason = d.pop("reason", UNSET)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        at = d.pop("at", UNSET)

        purchase_order_cost_center_change = cls(
            from_=from_,
            to=to,
            reason=reason,
            by=by,
            by_name=by_name,
            at=at,
        )

        purchase_order_cost_center_change.additional_properties = d
        return purchase_order_cost_center_change

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
