from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_rate_warning_object import (
    InvoiceRateWarningObject,
    check_invoice_rate_warning_object,
)
from ..models.invoice_rate_warning_source import (
    InvoiceRateWarningSource,
    check_invoice_rate_warning_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceRateWarning")


@_attrs_define
class InvoiceRateWarning:
    """
    Attributes:
        object_ (Union[Unset, InvoiceRateWarningObject]):
        currency (Union[Unset, str]):
        stated_rate (Union[Unset, float]):
        reference_rate (Union[Unset, float]):
        source (Union[Unset, InvoiceRateWarningSource]):
        as_of (Union[Unset, str]):
        deviation_pct (Union[Unset, float]):
    """

    object_: Union[Unset, InvoiceRateWarningObject] = UNSET
    currency: Union[Unset, str] = UNSET
    stated_rate: Union[Unset, float] = UNSET
    reference_rate: Union[Unset, float] = UNSET
    source: Union[Unset, InvoiceRateWarningSource] = UNSET
    as_of: Union[Unset, str] = UNSET
    deviation_pct: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_: Union[Unset, str] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_

        currency = self.currency

        stated_rate = self.stated_rate

        reference_rate = self.reference_rate

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        as_of = self.as_of

        deviation_pct = self.deviation_pct

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_ is not UNSET:
            field_dict["object"] = object_
        if currency is not UNSET:
            field_dict["currency"] = currency
        if stated_rate is not UNSET:
            field_dict["statedRate"] = stated_rate
        if reference_rate is not UNSET:
            field_dict["referenceRate"] = reference_rate
        if source is not UNSET:
            field_dict["source"] = source
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if deviation_pct is not UNSET:
            field_dict["deviationPct"] = deviation_pct

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, InvoiceRateWarningObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = check_invoice_rate_warning_object(_object_)

        currency = d.pop("currency", UNSET)

        stated_rate = d.pop("statedRate", UNSET)

        reference_rate = d.pop("referenceRate", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, InvoiceRateWarningSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_invoice_rate_warning_source(_source)

        as_of = d.pop("asOf", UNSET)

        deviation_pct = d.pop("deviationPct", UNSET)

        invoice_rate_warning = cls(
            object_=object_,
            currency=currency,
            stated_rate=stated_rate,
            reference_rate=reference_rate,
            source=source,
            as_of=as_of,
            deviation_pct=deviation_pct,
        )

        invoice_rate_warning.additional_properties = d
        return invoice_rate_warning

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
