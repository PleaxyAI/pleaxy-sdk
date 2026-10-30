from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_usage_line_invoicer import (
    AiUsageLineInvoicer,
    check_ai_usage_line_invoicer,
)
from ..models.ai_usage_line_meter import AiUsageLineMeter, check_ai_usage_line_meter
from ..models.ai_usage_line_shape import AiUsageLineShape, check_ai_usage_line_shape
from ..models.ai_usage_line_source import AiUsageLineSource, check_ai_usage_line_source
from ..models.ai_usage_line_unit import AiUsageLineUnit, check_ai_usage_line_unit
from ..models.ai_usage_line_vendor import AiUsageLineVendor, check_ai_usage_line_vendor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_usage_line_attribution import AiUsageLineAttribution
    from ..models.ai_usage_line_credits import AiUsageLineCredits


T = TypeVar("T", bound="AiUsageLine")


@_attrs_define
class AiUsageLine:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiUsageLineInvoicer]):
        vendor (Union[Unset, AiUsageLineVendor]):
        model (Union[Unset, str]):
        shape (Union[Unset, AiUsageLineShape]):
        meter (Union[Unset, AiUsageLineMeter]):
        region (Union[Unset, str]):
        day (Union[Unset, str]):
        quantity (Union[Unset, float]):
        unit (Union[Unset, AiUsageLineUnit]):
        credits_ (Union[Unset, AiUsageLineCredits]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        unit_price (Union[Unset, float]):
        attribution (Union[Unset, AiUsageLineAttribution]):
        source (Union[Unset, AiUsageLineSource]):
        raw_service (Union[Unset, str]):
        raw_usage_type (Union[Unset, str]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiUsageLineInvoicer] = UNSET
    vendor: Union[Unset, AiUsageLineVendor] = UNSET
    model: Union[Unset, str] = UNSET
    shape: Union[Unset, AiUsageLineShape] = UNSET
    meter: Union[Unset, AiUsageLineMeter] = UNSET
    region: Union[Unset, str] = UNSET
    day: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit: Union[Unset, AiUsageLineUnit] = UNSET
    credits_: Union[Unset, "AiUsageLineCredits"] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    attribution: Union[Unset, "AiUsageLineAttribution"] = UNSET
    source: Union[Unset, AiUsageLineSource] = UNSET
    raw_service: Union[Unset, str] = UNSET
    raw_usage_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        vendor: Union[Unset, str] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        model = self.model

        shape: Union[Unset, str] = UNSET
        if not isinstance(self.shape, Unset):
            shape = self.shape

        meter: Union[Unset, str] = UNSET
        if not isinstance(self.meter, Unset):
            meter = self.meter

        region = self.region

        day = self.day

        quantity = self.quantity

        unit: Union[Unset, str] = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

        credits_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = self.credits_.to_dict()

        amount = self.amount

        currency = self.currency

        unit_price = self.unit_price

        attribution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        raw_service = self.raw_service

        raw_usage_type = self.raw_usage_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if shape is not UNSET:
            field_dict["shape"] = shape
        if meter is not UNSET:
            field_dict["meter"] = meter
        if region is not UNSET:
            field_dict["region"] = region
        if day is not UNSET:
            field_dict["day"] = day
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if source is not UNSET:
            field_dict["source"] = source
        if raw_service is not UNSET:
            field_dict["rawService"] = raw_service
        if raw_usage_type is not UNSET:
            field_dict["rawUsageType"] = raw_usage_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_usage_line_attribution import AiUsageLineAttribution
        from ..models.ai_usage_line_credits import AiUsageLineCredits

        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiUsageLineInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_usage_line_invoicer(_invoicer)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, AiUsageLineVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = check_ai_usage_line_vendor(_vendor)

        model = d.pop("model", UNSET)

        _shape = d.pop("shape", UNSET)
        shape: Union[Unset, AiUsageLineShape]
        if isinstance(_shape, Unset):
            shape = UNSET
        else:
            shape = check_ai_usage_line_shape(_shape)

        _meter = d.pop("meter", UNSET)
        meter: Union[Unset, AiUsageLineMeter]
        if isinstance(_meter, Unset):
            meter = UNSET
        else:
            meter = check_ai_usage_line_meter(_meter)

        region = d.pop("region", UNSET)

        day = d.pop("day", UNSET)

        quantity = d.pop("quantity", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: Union[Unset, AiUsageLineUnit]
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_ai_usage_line_unit(_unit)

        _credits_ = d.pop("credits", UNSET)
        credits_: Union[Unset, AiUsageLineCredits]
        if isinstance(_credits_, Unset):
            credits_ = UNSET
        else:
            credits_ = AiUsageLineCredits.from_dict(_credits_)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        _attribution = d.pop("attribution", UNSET)
        attribution: Union[Unset, AiUsageLineAttribution]
        if isinstance(_attribution, Unset):
            attribution = UNSET
        else:
            attribution = AiUsageLineAttribution.from_dict(_attribution)

        _source = d.pop("source", UNSET)
        source: Union[Unset, AiUsageLineSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_ai_usage_line_source(_source)

        raw_service = d.pop("rawService", UNSET)

        raw_usage_type = d.pop("rawUsageType", UNSET)

        ai_usage_line = cls(
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            vendor=vendor,
            model=model,
            shape=shape,
            meter=meter,
            region=region,
            day=day,
            quantity=quantity,
            unit=unit,
            credits_=credits_,
            amount=amount,
            currency=currency,
            unit_price=unit_price,
            attribution=attribution,
            source=source,
            raw_service=raw_service,
            raw_usage_type=raw_usage_type,
        )

        ai_usage_line.additional_properties = d
        return ai_usage_line

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
