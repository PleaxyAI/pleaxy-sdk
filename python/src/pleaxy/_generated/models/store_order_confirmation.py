from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.store_order_confirmation_type import (
    StoreOrderConfirmationType,
    check_store_order_confirmation_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_order_confirmation_lines_item import (
        StoreOrderConfirmationLinesItem,
    )


T = TypeVar("T", bound="StoreOrderConfirmation")


@_attrs_define
class StoreOrderConfirmation:
    """
    Attributes:
        type (Union[Unset, StoreOrderConfirmationType]):
        at (Union[Unset, str]):
        store_confirmation_id (Union[Unset, str]):
        lines (Union[Unset, List['StoreOrderConfirmationLinesItem']]):
    """

    type: Union[Unset, StoreOrderConfirmationType] = UNSET
    at: Union[Unset, str] = UNSET
    store_confirmation_id: Union[Unset, str] = UNSET
    lines: Union[Unset, List["StoreOrderConfirmationLinesItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        at = self.at

        store_confirmation_id = self.store_confirmation_id

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if at is not UNSET:
            field_dict["at"] = at
        if store_confirmation_id is not UNSET:
            field_dict["storeConfirmationId"] = store_confirmation_id
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.store_order_confirmation_lines_item import (
            StoreOrderConfirmationLinesItem,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, StoreOrderConfirmationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_store_order_confirmation_type(_type)

        at = d.pop("at", UNSET)

        store_confirmation_id = d.pop("storeConfirmationId", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = StoreOrderConfirmationLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        store_order_confirmation = cls(
            type=type,
            at=at,
            store_confirmation_id=store_confirmation_id,
            lines=lines,
        )

        store_order_confirmation.additional_properties = d
        return store_order_confirmation

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
