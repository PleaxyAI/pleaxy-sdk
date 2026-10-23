from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_confirmation import OrderConfirmation
    from ..models.purchase_order import PurchaseOrder


T = TypeVar("T", bound="ApplyConfirmationChangesResult")


@_attrs_define
class ApplyConfirmationChangesResult:
    """
    Attributes:
        purchase_order (Union[Unset, PurchaseOrder]):
        confirmation (Union[Unset, OrderConfirmation]):
    """

    purchase_order: Union[Unset, "PurchaseOrder"] = UNSET
    confirmation: Union[Unset, "OrderConfirmation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        purchase_order: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.purchase_order, Unset):
            purchase_order = self.purchase_order.to_dict()

        confirmation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmation, Unset):
            confirmation = self.confirmation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_order is not UNSET:
            field_dict["purchaseOrder"] = purchase_order
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_confirmation import OrderConfirmation
        from ..models.purchase_order import PurchaseOrder

        d = src_dict.copy()
        _purchase_order = d.pop("purchaseOrder", UNSET)
        purchase_order: Union[Unset, PurchaseOrder]
        if isinstance(_purchase_order, Unset):
            purchase_order = UNSET
        else:
            purchase_order = PurchaseOrder.from_dict(_purchase_order)

        _confirmation = d.pop("confirmation", UNSET)
        confirmation: Union[Unset, OrderConfirmation]
        if isinstance(_confirmation, Unset):
            confirmation = UNSET
        else:
            confirmation = OrderConfirmation.from_dict(_confirmation)

        apply_confirmation_changes_result = cls(
            purchase_order=purchase_order,
            confirmation=confirmation,
        )

        apply_confirmation_changes_result.additional_properties = d
        return apply_confirmation_changes_result

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
