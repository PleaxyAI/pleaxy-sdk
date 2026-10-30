from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_rate_card_entry_invoicer import (
    AiRateCardEntryInvoicer,
    check_ai_rate_card_entry_invoicer,
)
from ..models.ai_rate_card_entry_meter import (
    AiRateCardEntryMeter,
    check_ai_rate_card_entry_meter,
)
from ..models.ai_rate_card_entry_unit import (
    AiRateCardEntryUnit,
    check_ai_rate_card_entry_unit,
)
from ..models.ai_rate_card_entry_vendor import (
    AiRateCardEntryVendor,
    check_ai_rate_card_entry_vendor,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiRateCardEntry")


@_attrs_define
class AiRateCardEntry:
    """
    Attributes:
        invoicer (Union[Unset, AiRateCardEntryInvoicer]):
        vendor (Union[Unset, AiRateCardEntryVendor]):
        model (Union[Unset, str]):
        meter (Union[Unset, AiRateCardEntryMeter]):
        region (Union[Unset, str]):
        unit (Union[Unset, AiRateCardEntryUnit]):
        unit_price (Union[Unset, float]):
        currency (Union[Unset, str]):
        effective_from (Union[Unset, str]):
        effective_to (Union[Unset, str]):
        source_url (Union[Unset, str]):
    """

    invoicer: Union[Unset, AiRateCardEntryInvoicer] = UNSET
    vendor: Union[Unset, AiRateCardEntryVendor] = UNSET
    model: Union[Unset, str] = UNSET
    meter: Union[Unset, AiRateCardEntryMeter] = UNSET
    region: Union[Unset, str] = UNSET
    unit: Union[Unset, AiRateCardEntryUnit] = UNSET
    unit_price: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    effective_from: Union[Unset, str] = UNSET
    effective_to: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
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

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

        unit_price = self.unit_price

        currency = self.currency

        effective_from = self.effective_from

        effective_to = self.effective_to

        source_url = self.source_url

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
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if effective_from is not UNSET:
            field_dict["effectiveFrom"] = effective_from
        if effective_to is not UNSET:
            field_dict["effectiveTo"] = effective_to
        if source_url is not UNSET:
            field_dict["sourceUrl"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiRateCardEntryInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_rate_card_entry_invoicer(_invoicer)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, AiRateCardEntryVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = check_ai_rate_card_entry_vendor(_vendor)

        model = d.pop("model", UNSET)

        _meter = d.pop("meter", UNSET)
        meter: Union[Unset, AiRateCardEntryMeter]
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = check_ai_rate_card_entry_meter(_meter)

        region = d.pop("region", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, AiRateCardEntryUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_ai_rate_card_entry_unit(_unit)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        effective_from = d.pop("effectiveFrom", UNSET)

        effective_to = d.pop("effectiveTo", UNSET)

        source_url = d.pop("sourceUrl", UNSET)

        ai_rate_card_entry = cls(
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            meter=meter,
            region=region,
            unit=unit,
            unit_price=unit_price,
            currency=currency,
            effective_from=effective_from,
            effective_to=effective_to,
            source_url=source_url,
        )

        ai_rate_card_entry.additional_properties = d
        return ai_rate_card_entry

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
