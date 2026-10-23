from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReceiptReversal")


@_attrs_define
class ReceiptReversal:
    """
    Attributes:
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        at (Union[Unset, str]):
        reason (Union[Unset, str]):
    """

    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        by = self.by

        by_name = self.by_name

        at = self.at

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if at is not UNSET:
            field_dict["at"] = at
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        at = d.pop("at", UNSET)

        reason = d.pop("reason", UNSET)

        receipt_reversal = cls(
            by=by,
            by_name=by_name,
            at=at,
            reason=reason,
        )

        receipt_reversal.additional_properties = d
        return receipt_reversal

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
