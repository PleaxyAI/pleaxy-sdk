from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_settlement_source import (
    InvoiceSettlementSource,
    check_invoice_settlement_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceSettlement")


@_attrs_define
class InvoiceSettlement:
    """
    Attributes:
        at (Union[Unset, str]):
        source (Union[Unset, InvoiceSettlementSource]):
        by (Union[Unset, str]):
        by_name (Union[Unset, str]):
        note (Union[Unset, str]):
        undo_until (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    source: Union[Unset, InvoiceSettlementSource] = UNSET
    by: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    undo_until: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        by = self.by

        by_name = self.by_name

        note = self.note

        undo_until = self.undo_until

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if source is not UNSET:
            field_dict["source"] = source
        if by is not UNSET:
            field_dict["by"] = by
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if note is not UNSET:
            field_dict["note"] = note
        if undo_until is not UNSET:
            field_dict["undoUntil"] = undo_until

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, InvoiceSettlementSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_invoice_settlement_source(_source)

        by = d.pop("by", UNSET)

        by_name = d.pop("byName", UNSET)

        note = d.pop("note", UNSET)

        undo_until = d.pop("undoUntil", UNSET)

        invoice_settlement = cls(
            at=at,
            source=source,
            by=by,
            by_name=by_name,
            note=note,
            undo_until=undo_until,
        )

        invoice_settlement.additional_properties = d
        return invoice_settlement

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
