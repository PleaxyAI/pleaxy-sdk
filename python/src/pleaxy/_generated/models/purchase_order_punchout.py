from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purchase_order_punchout_claimed import PurchaseOrderPunchoutClaimed


T = TypeVar("T", bound="PurchaseOrderPunchout")


@_attrs_define
class PurchaseOrderPunchout:
    """
    Attributes:
        claimed (Union[Unset, PurchaseOrderPunchoutClaimed]):
    """

    claimed: Union[Unset, "PurchaseOrderPunchoutClaimed"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        claimed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claimed, Unset):
            claimed = self.claimed.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if claimed is not UNSET:
            field_dict["claimed"] = claimed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.purchase_order_punchout_claimed import (
            PurchaseOrderPunchoutClaimed,
        )

        d = src_dict.copy()
        _claimed = d.pop("claimed", UNSET)
        claimed: Union[Unset, PurchaseOrderPunchoutClaimed]
        if isinstance(_claimed, Unset):
            claimed = UNSET
        else:
            claimed = PurchaseOrderPunchoutClaimed.from_dict(_claimed)

        purchase_order_punchout = cls(
            claimed=claimed,
        )

        purchase_order_punchout.additional_properties = d
        return purchase_order_punchout

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
