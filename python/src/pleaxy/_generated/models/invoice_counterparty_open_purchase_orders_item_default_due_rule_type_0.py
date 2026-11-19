from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0_from import (
    InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From,
    check_invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0_from,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0")


@_attrs_define
class InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0:
    """
    Attributes:
        from_ (Union[Unset, InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From]):
        days (Union[Unset, float]):
    """

    from_: Union[
        Unset, InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From
    ] = UNSET
    days: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_

        days = self.days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[
            Unset, InvoiceCounterpartyOpenPurchaseOrdersItemDefaultDueRuleType0From
        ]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = check_invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0_from(
                _from_
            )

        days = d.pop("days", UNSET)

        invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0 = cls(
            from_=from_,
            days=days,
        )

        invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0.additional_properties = d
        return invoice_counterparty_open_purchase_orders_item_default_due_rule_type_0

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
