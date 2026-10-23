from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_order_confirmation_input_type import (
    CreateOrderConfirmationInputType,
    check_create_order_confirmation_input_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_confirmation_line_input import OrderConfirmationLineInput


T = TypeVar("T", bound="CreateOrderConfirmationInput")


@_attrs_define
class CreateOrderConfirmationInput:
    """
    Attributes:
        type (CreateOrderConfirmationInputType):
        confirm_id (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        note (Union[Unset, str]):
        lines (Union[Unset, List['OrderConfirmationLineInput']]):
    """

    type: CreateOrderConfirmationInputType
    confirm_id: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    lines: Union[Unset, List["OrderConfirmationLineInput"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: str = self.type

        confirm_id = self.confirm_id

        delivery_date = self.delivery_date

        note = self.note

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if confirm_id is not UNSET:
            field_dict["confirmId"] = confirm_id
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if note is not UNSET:
            field_dict["note"] = note
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_confirmation_line_input import OrderConfirmationLineInput

        d = src_dict.copy()
        type = check_create_order_confirmation_input_type(d.pop("type"))

        confirm_id = d.pop("confirmId", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        note = d.pop("note", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = OrderConfirmationLineInput.from_dict(lines_item_data)

            lines.append(lines_item)

        create_order_confirmation_input = cls(
            type=type,
            confirm_id=confirm_id,
            delivery_date=delivery_date,
            note=note,
            lines=lines,
        )

        create_order_confirmation_input.additional_properties = d
        return create_order_confirmation_input

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
