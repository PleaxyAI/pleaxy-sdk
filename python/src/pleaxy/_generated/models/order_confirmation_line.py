from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_confirmation_line_status import (
    OrderConfirmationLineStatus,
    check_order_confirmation_line_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderConfirmationLine")


@_attrs_define
class OrderConfirmationLine:
    """
    Attributes:
        line_no (Union[Unset, float]):
        status (Union[Unset, OrderConfirmationLineStatus]):
        qty (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        shipment_date (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        reason (Union[Unset, str]):
    """

    line_no: Union[Unset, float] = UNSET
    status: Union[Unset, OrderConfirmationLineStatus] = UNSET
    qty: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    shipment_date: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        qty = self.qty

        unit_price = self.unit_price

        shipment_date = self.shipment_date

        delivery_date = self.delivery_date

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if status is not UNSET:
            field_dict["status"] = status
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderConfirmationLineStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_order_confirmation_line_status(_status)

        qty = d.pop("qty", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        shipment_date = d.pop("shipmentDate", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        reason = d.pop("reason", UNSET)

        order_confirmation_line = cls(
            line_no=line_no,
            status=status,
            qty=qty,
            unit_price=unit_price,
            shipment_date=shipment_date,
            delivery_date=delivery_date,
            reason=reason,
        )

        order_confirmation_line.additional_properties = d
        return order_confirmation_line

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
