from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_email_draft_confirmation_lines_item_status import (
    InboundEmailDraftConfirmationLinesItemStatus,
    check_inbound_email_draft_confirmation_lines_item_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_confirmation_substitute import OrderConfirmationSubstitute


T = TypeVar("T", bound="InboundEmailDraftConfirmationLinesItem")


@_attrs_define
class InboundEmailDraftConfirmationLinesItem:
    """
    Attributes:
        line_no (Union[Unset, float]):
        status (Union[Unset, InboundEmailDraftConfirmationLinesItemStatus]):
        qty (Union[Unset, float]):
        unit_price (Union[Unset, float]):
        substitute (Union[Unset, OrderConfirmationSubstitute]):
        shipment_date (Union[Unset, str]):
        delivery_date (Union[Unset, str]):
        reason (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    line_no: Union[Unset, float] = UNSET
    status: Union[Unset, InboundEmailDraftConfirmationLinesItemStatus] = UNSET
    qty: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    substitute: Union[Unset, "OrderConfirmationSubstitute"] = UNSET
    shipment_date: Union[Unset, str] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        qty = self.qty

        unit_price = self.unit_price

        substitute: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.substitute, Unset):
            substitute = self.substitute.to_dict()

        shipment_date = self.shipment_date

        delivery_date = self.delivery_date

        reason = self.reason

        currency = self.currency

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
        if substitute is not UNSET:
            field_dict["substitute"] = substitute
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if reason is not UNSET:
            field_dict["reason"] = reason
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_confirmation_substitute import OrderConfirmationSubstitute

        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InboundEmailDraftConfirmationLinesItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_inbound_email_draft_confirmation_lines_item_status(_status)

        qty = d.pop("qty", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        _substitute = d.pop("substitute", UNSET)
        substitute: Union[Unset, OrderConfirmationSubstitute]
        if isinstance(_substitute, Unset):
            substitute = UNSET
        else:
            substitute = OrderConfirmationSubstitute.from_dict(_substitute)

        shipment_date = d.pop("shipmentDate", UNSET)

        delivery_date = d.pop("deliveryDate", UNSET)

        reason = d.pop("reason", UNSET)

        currency = d.pop("currency", UNSET)

        inbound_email_draft_confirmation_lines_item = cls(
            line_no=line_no,
            status=status,
            qty=qty,
            unit_price=unit_price,
            substitute=substitute,
            shipment_date=shipment_date,
            delivery_date=delivery_date,
            reason=reason,
            currency=currency,
        )

        inbound_email_draft_confirmation_lines_item.additional_properties = d
        return inbound_email_draft_confirmation_lines_item

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
