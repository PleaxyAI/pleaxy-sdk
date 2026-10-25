from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_billing_previous_finalized_invoice_source import (
    CloudConnectionBillingPreviousFinalizedInvoiceSource,
    check_cloud_connection_billing_previous_finalized_invoice_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionBillingPreviousFinalizedInvoice")


@_attrs_define
class CloudConnectionBillingPreviousFinalizedInvoice:
    """
    Attributes:
        period_label (Union[Unset, str]):
        total_amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        source (Union[Unset, CloudConnectionBillingPreviousFinalizedInvoiceSource]):
    """

    period_label: Union[Unset, str] = UNSET
    total_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    source: Union[Unset, CloudConnectionBillingPreviousFinalizedInvoiceSource] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period_label = self.period_label

        total_amount = self.total_amount

        currency = self.currency

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period_label is not UNSET:
            field_dict["periodLabel"] = period_label
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        period_label = d.pop("periodLabel", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        currency = d.pop("currency", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CloudConnectionBillingPreviousFinalizedInvoiceSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_cloud_connection_billing_previous_finalized_invoice_source(
                _source
            )

        cloud_connection_billing_previous_finalized_invoice = cls(
            period_label=period_label,
            total_amount=total_amount,
            currency=currency,
            source=source,
        )

        cloud_connection_billing_previous_finalized_invoice.additional_properties = d
        return cloud_connection_billing_previous_finalized_invoice

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
