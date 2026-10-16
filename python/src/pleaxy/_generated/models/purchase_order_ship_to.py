from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postal_address import PostalAddress


T = TypeVar("T", bound="PurchaseOrderShipTo")


@_attrs_define
class PurchaseOrderShipTo:
    """
    Attributes:
        address_id (Union[Unset, str]):
        label (Union[Unset, str]):
        attention (Union[Unset, str]):
        address (Union[Unset, PostalAddress]):
        phone (Union[Unset, str]):
    """

    address_id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    attention: Union[Unset, str] = UNSET
    address: Union[Unset, "PostalAddress"] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_id = self.address_id

        label = self.label

        attention = self.attention

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        phone = self.phone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if label is not UNSET:
            field_dict["label"] = label
        if attention is not UNSET:
            field_dict["attention"] = attention
        if address is not UNSET:
            field_dict["address"] = address
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postal_address import PostalAddress

        d = src_dict.copy()
        address_id = d.pop("addressId", UNSET)

        label = d.pop("label", UNSET)

        attention = d.pop("attention", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, PostalAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = PostalAddress.from_dict(_address)

        phone = d.pop("phone", UNSET)

        purchase_order_ship_to = cls(
            address_id=address_id,
            label=label,
            attention=attention,
            address=address,
            phone=phone,
        )

        purchase_order_ship_to.additional_properties = d
        return purchase_order_ship_to

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
