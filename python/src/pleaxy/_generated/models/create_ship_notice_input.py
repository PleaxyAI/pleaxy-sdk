from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_ship_notice_input_status import (
    CreateShipNoticeInputStatus,
    check_create_ship_notice_input_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_notice_line_input import ShipNoticeLineInput


T = TypeVar("T", bound="CreateShipNoticeInput")


@_attrs_define
class CreateShipNoticeInput:
    """
    Attributes:
        shipment_id (str):
        status (Union[Unset, CreateShipNoticeInputStatus]):
        shipment_date (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        carrier (Union[Unset, str]):
        tracking_number (Union[Unset, str]):
        tracking_url (Union[Unset, str]):
        note (Union[Unset, str]):
        lines (Union[Unset, List['ShipNoticeLineInput']]):
    """

    shipment_id: str
    status: Union[Unset, CreateShipNoticeInputStatus] = UNSET
    shipment_date: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    lines: Union[Unset, List["ShipNoticeLineInput"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        shipment_date = self.shipment_date

        delivery_date = self.delivery_date

        carrier = self.carrier

        tracking_number = self.tracking_number

        tracking_url = self.tracking_url

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
                "shipmentId": shipment_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if tracking_url is not UNSET:
            field_dict["trackingUrl"] = tracking_url
        if note is not UNSET:
            field_dict["note"] = note
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_notice_line_input import ShipNoticeLineInput

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId")

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateShipNoticeInputStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_create_ship_notice_input_status(_status)

        shipment_date = d.pop("shipmentDate", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        carrier = d.pop("carrier", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        note = d.pop("note", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ShipNoticeLineInput.from_dict(lines_item_data)

            lines.append(lines_item)

        create_ship_notice_input = cls(
            shipment_id=shipment_id,
            status=status,
            shipment_date=shipment_date,
            delivery_date=delivery_date,
            carrier=carrier,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            note=note,
            lines=lines,
        )

        create_ship_notice_input.additional_properties = d
        return create_ship_notice_input

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
