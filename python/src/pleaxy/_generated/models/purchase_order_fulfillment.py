from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_confirmation import OrderConfirmation
    from ..models.purchase_order_fulfillment_shipped_by_line_item import (
        PurchaseOrderFulfillmentShippedByLineItem,
    )
    from ..models.ship_notice import ShipNotice


T = TypeVar("T", bound="PurchaseOrderFulfillment")


@_attrs_define
class PurchaseOrderFulfillment:
    """
    Attributes:
        confirmation (Union[Unset, OrderConfirmation]):
        confirmations (Union[Unset, List['OrderConfirmation']]):
        ship_notices (Union[Unset, List['ShipNotice']]):
        shipped_by_line (Union[Unset, List['PurchaseOrderFulfillmentShippedByLineItem']]):
        expected_delivery_date (Union[Unset, str]):
    """

    confirmation: Union[Unset, "OrderConfirmation"] = UNSET
    confirmations: Union[Unset, List["OrderConfirmation"]] = UNSET
    ship_notices: Union[Unset, List["ShipNotice"]] = UNSET
    shipped_by_line: Union[Unset, List["PurchaseOrderFulfillmentShippedByLineItem"]] = (
        UNSET
    )
    expected_delivery_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmation, Unset):
            confirmation = self.confirmation.to_dict()

        confirmations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.confirmations, Unset):
            confirmations = []
            for confirmations_item_data in self.confirmations:
                confirmations_item = confirmations_item_data.to_dict()
                confirmations.append(confirmations_item)

        ship_notices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ship_notices, Unset):
            ship_notices = []
            for ship_notices_item_data in self.ship_notices:
                ship_notices_item = ship_notices_item_data.to_dict()
                ship_notices.append(ship_notices_item)

        shipped_by_line: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shipped_by_line, Unset):
            shipped_by_line = []
            for shipped_by_line_item_data in self.shipped_by_line:
                shipped_by_line_item = shipped_by_line_item_data.to_dict()
                shipped_by_line.append(shipped_by_line_item)

        expected_delivery_date = self.expected_delivery_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if confirmations is not UNSET:
            field_dict["confirmations"] = confirmations
        if ship_notices is not UNSET:
            field_dict["shipNotices"] = ship_notices
        if shipped_by_line is not UNSET:
            field_dict["shippedByLine"] = shipped_by_line
        if expected_delivery_date is not UNSET:
            field_dict["expectedDeliveryDate"] = expected_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_confirmation import OrderConfirmation
        from ..models.purchase_order_fulfillment_shipped_by_line_item import (
            PurchaseOrderFulfillmentShippedByLineItem,
        )
        from ..models.ship_notice import ShipNotice

        d = src_dict.copy()
        _confirmation = d.pop("confirmation", UNSET)
        confirmation: Union[Unset, OrderConfirmation]
        if isinstance(_confirmation, Unset):
            confirmation = UNSET
        else:
            confirmation = OrderConfirmation.from_dict(_confirmation)

        confirmations = []
        _confirmations = d.pop("confirmations", UNSET)
        for confirmations_item_data in _confirmations or []:
            confirmations_item = OrderConfirmation.from_dict(confirmations_item_data)

            confirmations.append(confirmations_item)

        ship_notices = []
        _ship_notices = d.pop("shipNotices", UNSET)
        for ship_notices_item_data in _ship_notices or []:
            ship_notices_item = ShipNotice.from_dict(ship_notices_item_data)

            ship_notices.append(ship_notices_item)

        shipped_by_line = []
        _shipped_by_line = d.pop("shippedByLine", UNSET)
        for shipped_by_line_item_data in _shipped_by_line or []:
            shipped_by_line_item = PurchaseOrderFulfillmentShippedByLineItem.from_dict(
                shipped_by_line_item_data
            )

            shipped_by_line.append(shipped_by_line_item)

        expected_delivery_date = d.pop("expectedDeliveryDate", UNSET)

        purchase_order_fulfillment = cls(
            confirmation=confirmation,
            confirmations=confirmations,
            ship_notices=ship_notices,
            shipped_by_line=shipped_by_line,
            expected_delivery_date=expected_delivery_date,
        )

        purchase_order_fulfillment.additional_properties = d
        return purchase_order_fulfillment

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
