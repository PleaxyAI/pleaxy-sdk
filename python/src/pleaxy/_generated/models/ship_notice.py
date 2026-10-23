from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ship_notice_source import ShipNoticeSource, check_ship_notice_source
from ..models.ship_notice_status import ShipNoticeStatus, check_ship_notice_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ship_notice_line import ShipNoticeLine
    from ..models.ship_notice_receipts_item import ShipNoticeReceiptsItem


T = TypeVar("T", bound="ShipNotice")


@_attrs_define
class ShipNotice:
    """
    Attributes:
        shipment_id (Union[Unset, str]):
        po_id (Union[Unset, str]):
        status (Union[Unset, ShipNoticeStatus]):
        shipment_date (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        carrier (Union[Unset, str]):
        tracking_number (Union[Unset, str]):
        tracking_url (Union[Unset, str]):
        lines (Union[Unset, List['ShipNoticeLine']]):
        note (Union[Unset, str]):
        source (Union[Unset, ShipNoticeSource]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        receipts (Union[Unset, List['ShipNoticeReceiptsItem']]):
    """

    shipment_id: Union[Unset, str] = UNSET
    po_id: Union[Unset, str] = UNSET
    status: Union[Unset, ShipNoticeStatus] = UNSET
    shipment_date: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    lines: Union[Unset, List["ShipNoticeLine"]] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, ShipNoticeSource] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    receipts: Union[Unset, List["ShipNoticeReceiptsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shipment_id = self.shipment_id

        po_id = self.po_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        shipment_date = self.shipment_date

        delivery_date = self.delivery_date

        carrier = self.carrier

        tracking_number = self.tracking_number

        tracking_url = self.tracking_url

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        note = self.note

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        created_at = self.created_at

        updated_at = self.updated_at

        receipts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.receipts, Unset):
            receipts = []
            for receipts_item_data in self.receipts:
                receipts_item = receipts_item_data.to_dict()
                receipts.append(receipts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id
        if po_id is not UNSET:
            field_dict["poId"] = po_id
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
        if lines is not UNSET:
            field_dict["lines"] = lines
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if receipts is not UNSET:
            field_dict["receipts"] = receipts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ship_notice_line import ShipNoticeLine
        from ..models.ship_notice_receipts_item import ShipNoticeReceiptsItem

        d = src_dict.copy()
        shipment_id = d.pop("shipmentId", UNSET)

        po_id = d.pop("poId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ShipNoticeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_ship_notice_status(_status)

        shipment_date = d.pop("shipmentDate", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        carrier = d.pop("carrier", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        tracking_url = d.pop("trackingUrl", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = ShipNoticeLine.from_dict(lines_item_data)

            lines.append(lines_item)

        note = d.pop("note", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ShipNoticeSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_ship_notice_source(_source)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        receipts = []
        _receipts = d.pop("receipts", UNSET)
        for receipts_item_data in _receipts or []:
            receipts_item = ShipNoticeReceiptsItem.from_dict(receipts_item_data)

            receipts.append(receipts_item)

        ship_notice = cls(
            shipment_id=shipment_id,
            po_id=po_id,
            status=status,
            shipment_date=shipment_date,
            delivery_date=delivery_date,
            carrier=carrier,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            lines=lines,
            note=note,
            source=source,
            created_at=created_at,
            updated_at=updated_at,
            receipts=receipts,
        )

        ship_notice.additional_properties = d
        return ship_notice

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
