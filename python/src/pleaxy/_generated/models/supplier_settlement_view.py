from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_settlement_view_source import (
    SupplierSettlementViewSource,
    check_supplier_settlement_view_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierSettlementView")


@_attrs_define
class SupplierSettlementView:
    """
    Attributes:
        at (Union[Unset, str]):
        source (Union[Unset, SupplierSettlementViewSource]):
        undo_until (Union[Unset, str]):
        by_name (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    source: Union[Unset, SupplierSettlementViewSource] = UNSET
    undo_until: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        undo_until = self.undo_until

        by_name = self.by_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if source is not UNSET:
            field_dict["source"] = source
        if undo_until is not UNSET:
            field_dict["undoUntil"] = undo_until
        if by_name is not UNSET:
            field_dict["byName"] = by_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, SupplierSettlementViewSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_supplier_settlement_view_source(_source)

        undo_until = d.pop("undoUntil", UNSET)

        by_name = d.pop("byName", UNSET)

        supplier_settlement_view = cls(
            at=at,
            source=source,
            undo_until=undo_until,
            by_name=by_name,
        )

        supplier_settlement_view.additional_properties = d
        return supplier_settlement_view

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
