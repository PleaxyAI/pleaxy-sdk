from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_rate_attribution import ReferenceRateAttribution


T = TypeVar("T", bound="ReferenceRate")


@_attrs_define
class ReferenceRate:
    """
    Attributes:
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        rate (Union[Unset, float]):
        date (Union[Unset, str]):
        source (Union[Unset, str]):
        attribution (Union[Unset, ReferenceRateAttribution]):
    """

    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    date: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    attribution: Union[Unset, "ReferenceRateAttribution"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        rate = self.rate

        date = self.date

        source = self.source

        attribution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if rate is not UNSET:
            field_dict["rate"] = rate
        if date is not UNSET:
            field_dict["date"] = date
        if source is not UNSET:
            field_dict["source"] = source
        if attribution is not UNSET:
            field_dict["attribution"] = attribution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference_rate_attribution import ReferenceRateAttribution

        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        rate = d.pop("rate", UNSET)

        date = d.pop("date", UNSET)

        source = d.pop("source", UNSET)

        _attribution = d.pop("attribution", UNSET)
        attribution: Union[Unset, ReferenceRateAttribution]
        if isinstance(_attribution, Unset):
            attribution = UNSET
        else:
            attribution = ReferenceRateAttribution.from_dict(_attribution)

        reference_rate = cls(
            from_=from_,
            to=to,
            rate=rate,
            date=date,
            source=source,
            attribution=attribution,
        )

        reference_rate.additional_properties = d
        return reference_rate

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
