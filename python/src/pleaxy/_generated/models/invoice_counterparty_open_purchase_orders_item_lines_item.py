from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem")


@_attrs_define
class InvoiceCounterpartyOpenPurchaseOrdersItemLinesItem:
    """
    Attributes:
        line_no (Union[Unset, float]):
        name (Union[Unset, str]):
        amount (Union[Unset, float]):
        consumed (Union[Unset, float]):
    """

    line_no: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    consumed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        name = self.name

        amount = self.amount

        consumed = self.consumed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if consumed is not UNSET:
            field_dict["consumed"] = consumed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        name = d.pop("name", UNSET)

        amount = d.pop("amount", UNSET)

        consumed = d.pop("consumed", UNSET)

        invoice_counterparty_open_purchase_orders_item_lines_item = cls(
            line_no=line_no,
            name=name,
            amount=amount,
            consumed=consumed,
        )

        invoice_counterparty_open_purchase_orders_item_lines_item.additional_properties = d
        return invoice_counterparty_open_purchase_orders_item_lines_item

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
