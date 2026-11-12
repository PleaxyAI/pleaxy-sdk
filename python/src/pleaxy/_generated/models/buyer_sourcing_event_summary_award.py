from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_event_summary_award_order import (
    BuyerSourcingEventSummaryAwardOrder,
    check_buyer_sourcing_event_summary_award_order,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerSourcingEventSummaryAward")


@_attrs_define
class BuyerSourcingEventSummaryAward:
    """
    Attributes:
        supplier_name (Union[Unset, str]):
        currency (Union[Unset, str]):
        total (Union[Unset, float]):
        order (Union[Unset, BuyerSourcingEventSummaryAwardOrder]):
        po_id (Union[Unset, str]):
    """

    supplier_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    order: Union[Unset, BuyerSourcingEventSummaryAwardOrder] = UNSET
    po_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_name = self.supplier_name

        currency = self.currency

        total = self.total

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order

        po_id = self.po_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total is not UNSET:
            field_dict["total"] = total
        if order is not UNSET:
            field_dict["order"] = order
        if po_id is not UNSET:
            field_dict["poId"] = po_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_name = d.pop("supplierName", UNSET)

        currency = d.pop("currency", UNSET)

        total = d.pop("total", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, BuyerSourcingEventSummaryAwardOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = check_buyer_sourcing_event_summary_award_order(_order)

        po_id = d.pop("poId", UNSET)

        buyer_sourcing_event_summary_award = cls(
            supplier_name=supplier_name,
            currency=currency,
            total=total,
            order=order,
            po_id=po_id,
        )

        buyer_sourcing_event_summary_award.additional_properties = d
        return buyer_sourcing_event_summary_award

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
