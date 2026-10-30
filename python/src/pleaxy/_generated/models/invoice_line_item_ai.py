from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_line_item_ai_invoicer import (
    InvoiceLineItemAiInvoicer,
    check_invoice_line_item_ai_invoicer,
)
from ..models.invoice_line_item_ai_meter import (
    InvoiceLineItemAiMeter,
    check_invoice_line_item_ai_meter,
)
from ..models.invoice_line_item_ai_vendor import (
    InvoiceLineItemAiVendor,
    check_invoice_line_item_ai_vendor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceLineItemAi")


@_attrs_define
class InvoiceLineItemAi:
    """
    Attributes:
        invoicer (Union[Unset, InvoiceLineItemAiInvoicer]):
        vendor (Union[Unset, InvoiceLineItemAiVendor]):
        model (Union[Unset, str]):
        meter (Union[Unset, InvoiceLineItemAiMeter]):
        region (Union[Unset, str]):
        period (Union[Unset, str]):
    """

    invoicer: Union[Unset, InvoiceLineItemAiInvoicer] = UNSET
    vendor: Union[Unset, InvoiceLineItemAiVendor] = UNSET
    model: Union[Unset, str] = UNSET
    meter: Union[Unset, InvoiceLineItemAiMeter] = UNSET
    region: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        vendor: Union[Unset, str] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        model = self.model

        meter: Union[Unset, str] = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter

        region = self.region

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if meter is not UNSET:
            field_dict["meter"] = meter
        if region is not UNSET:
            field_dict["region"] = region
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, InvoiceLineItemAiInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_invoice_line_item_ai_invoicer(_invoicer)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, InvoiceLineItemAiVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = check_invoice_line_item_ai_vendor(_vendor)

        model = d.pop("model", UNSET)

        _meter = d.pop("meter", UNSET)
        meter: Union[Unset, InvoiceLineItemAiMeter]
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = check_invoice_line_item_ai_meter(_meter)

        region = d.pop("region", UNSET)

        period = d.pop("period", UNSET)

        invoice_line_item_ai = cls(
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            meter=meter,
            region=region,
            period=period,
        )

        invoice_line_item_ai.additional_properties = d
        return invoice_line_item_ai

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
