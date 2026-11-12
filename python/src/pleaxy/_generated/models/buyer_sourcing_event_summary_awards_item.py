from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_event_summary_awards_item_order import (
    BuyerSourcingEventSummaryAwardsItemOrder,
    check_buyer_sourcing_event_summary_awards_item_order,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerSourcingEventSummaryAwardsItem")


@_attrs_define
class BuyerSourcingEventSummaryAwardsItem:
    """
    Attributes:
        supplier_name (Union[Unset, str]):
        currency (Union[Unset, str]):
        contract_id (Union[Unset, str]):
        total (Union[Unset, float]):
        order (Union[Unset, BuyerSourcingEventSummaryAwardsItemOrder]):
        po_id (Union[Unset, str]):
        supplier_key (Union[Unset, str]):
    """

    supplier_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    order: Union[Unset, BuyerSourcingEventSummaryAwardsItemOrder] = UNSET
    po_id: Union[Unset, str] = UNSET
    supplier_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_name = self.supplier_name

        currency = self.currency

        contract_id = self.contract_id

        total = self.total

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order

        po_id = self.po_id

        supplier_key = self.supplier_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if total is not UNSET:
            field_dict["total"] = total
        if order is not UNSET:
            field_dict["order"] = order
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_name = d.pop("supplierName", UNSET)

        currency = d.pop("currency", UNSET)

        contract_id = d.pop("contractId", UNSET)

        total = d.pop("total", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, BuyerSourcingEventSummaryAwardsItemOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = check_buyer_sourcing_event_summary_awards_item_order(_order)

        po_id = d.pop("poId", UNSET)

        supplier_key = d.pop("supplierKey", UNSET)

        buyer_sourcing_event_summary_awards_item = cls(
            supplier_name=supplier_name,
            currency=currency,
            contract_id=contract_id,
            total=total,
            order=order,
            po_id=po_id,
            supplier_key=supplier_key,
        )

        buyer_sourcing_event_summary_awards_item.additional_properties = d
        return buyer_sourcing_event_summary_awards_item

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
