from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundEmailResult")


@_attrs_define
class InboundEmailResult:
    """
    Attributes:
        confirmation_id (Union[Unset, str]):
        shipment_id (Union[Unset, str]):
    """

    confirmation_id: Union[Unset, str] = UNSET
    shipment_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        confirmation_id = self.confirmation_id

        shipment_id = self.shipment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirmation_id is not UNSET:
            field_dict["confirmationId"] = confirmation_id
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        confirmation_id = d.pop("confirmationId", UNSET)

        shipment_id = d.pop("shipmentId", UNSET)

        inbound_email_result = cls(
            confirmation_id=confirmation_id,
            shipment_id=shipment_id,
        )

        inbound_email_result.additional_properties = d
        return inbound_email_result

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
