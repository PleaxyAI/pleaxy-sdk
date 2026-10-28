from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_screening_history_item_event import (
    SupplierScreeningHistoryItemEvent,
    check_supplier_screening_history_item_event,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupplierScreeningHistoryItem")


@_attrs_define
class SupplierScreeningHistoryItem:
    """
    Attributes:
        at (Union[Unset, str]):
        event (Union[Unset, SupplierScreeningHistoryItemEvent]):
        match_id (Union[Unset, str]):
        by (Union[Unset, str]):
    """

    at: Union[Unset, str] = UNSET
    event: Union[Unset, SupplierScreeningHistoryItemEvent] = UNSET
    match_id: Union[Unset, str] = UNSET
    by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event

        match_id = self.match_id

        by = self.by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if event is not UNSET:
            field_dict["event"] = event
        if match_id is not UNSET:
            field_dict["matchId"] = match_id
        if by is not UNSET:
            field_dict["by"] = by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _event = d.pop("event", UNSET)
        event: Union[Unset, SupplierScreeningHistoryItemEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = check_supplier_screening_history_item_event(_event)

        match_id = d.pop("matchId", UNSET)

        by = d.pop("by", UNSET)

        supplier_screening_history_item = cls(
            at=at,
            event=event,
            match_id=match_id,
            by=by,
        )

        supplier_screening_history_item.additional_properties = d
        return supplier_screening_history_item

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
