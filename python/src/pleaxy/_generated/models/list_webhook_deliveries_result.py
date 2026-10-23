from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_delivery import WebhookDelivery


T = TypeVar("T", bound="ListWebhookDeliveriesResult")


@_attrs_define
class ListWebhookDeliveriesResult:
    """
    Attributes:
        deliveries (Union[Unset, List['WebhookDelivery']]):
    """

    deliveries: Union[Unset, List["WebhookDelivery"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deliveries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deliveries, Unset):
            deliveries = []
            for deliveries_item_data in self.deliveries:
                deliveries_item = deliveries_item_data.to_dict()
                deliveries.append(deliveries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deliveries is not UNSET:
            field_dict["deliveries"] = deliveries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_delivery import WebhookDelivery

        d = src_dict.copy()
        deliveries = []
        _deliveries = d.pop("deliveries", UNSET)
        for deliveries_item_data in _deliveries or []:
            deliveries_item = WebhookDelivery.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        list_webhook_deliveries_result = cls(
            deliveries=deliveries,
        )

        list_webhook_deliveries_result.additional_properties = d
        return list_webhook_deliveries_result

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
