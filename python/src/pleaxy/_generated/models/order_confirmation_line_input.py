from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_confirmation_line_input_status import (
    OrderConfirmationLineInputStatus,
    check_order_confirmation_line_input_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.substitute_item_input import SubstituteItemInput


T = TypeVar("T", bound="OrderConfirmationLineInput")


@_attrs_define
class OrderConfirmationLineInput:
    """
    Attributes:
        line_no (float):
        status (OrderConfirmationLineInputStatus):
        qty (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        substitute (Union[Unset, SubstituteItemInput]):
        shipment_date (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        reason (Union[Unset, str]):
    """

    line_no: float
    status: OrderConfirmationLineInputStatus
    qty: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    substitute: Union[Unset, "SubstituteItemInput"] = UNSET
    shipment_date: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        status: str = self.status

        qty = self.qty

        unit_price = self.unit_price

        substitute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substitute, Unset):
            substitute = self.substitute.to_dict()

        shipment_date = self.shipment_date

        delivery_date = self.delivery_date

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNo": line_no,
                "status": status,
            }
        )
        if qty is not UNSET:
            field_dict["qty"] = qty
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if substitute is not UNSET:
            field_dict["substitute"] = substitute
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.substitute_item_input import SubstituteItemInput

        d = src_dict.copy()
        line_no = d.pop("lineNo")

        status = check_order_confirmation_line_input_status(d.pop("status"))

        qty = d.pop("qty", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        _substitute = d.pop("substitute", UNSET)
        substitute: Union[Unset, SubstituteItemInput]
        if isinstance(_substitute, Unset):
            substitute = UNSET
        else:
            substitute = SubstituteItemInput.from_dict(_substitute)

        shipment_date = d.pop("shipmentDate", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        reason = d.pop("reason", UNSET)

        order_confirmation_line_input = cls(
            line_no=line_no,
            status=status,
            qty=qty,
            unit_price=unit_price,
            substitute=substitute,
            shipment_date=shipment_date,
            delivery_date=delivery_date,
            reason=reason,
        )

        order_confirmation_line_input.additional_properties = d
        return order_confirmation_line_input

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
