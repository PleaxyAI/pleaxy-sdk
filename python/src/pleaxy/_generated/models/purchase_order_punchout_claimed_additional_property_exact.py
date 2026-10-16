from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PurchaseOrderPunchoutClaimedAdditionalPropertyExact")


@_attrs_define
class PurchaseOrderPunchoutClaimedAdditionalPropertyExact:
    """
    Attributes:
        cart_lines (Union[Unset, float]):
    """

    cart_lines: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cart_lines = self.cart_lines

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cart_lines is not UNSET:
            field_dict["cartLines"] = cart_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cart_lines = d.pop("cartLines", UNSET)

        purchase_order_punchout_claimed_additional_property_exact = cls(
            cart_lines=cart_lines,
        )

        purchase_order_punchout_claimed_additional_property_exact.additional_properties = d
        return purchase_order_punchout_claimed_additional_property_exact

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
