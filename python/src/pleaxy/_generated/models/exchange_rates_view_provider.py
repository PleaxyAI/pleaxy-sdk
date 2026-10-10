from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_rates_view_provider_attribution import (
        ExchangeRatesViewProviderAttribution,
    )


T = TypeVar("T", bound="ExchangeRatesViewProvider")


@_attrs_define
class ExchangeRatesViewProvider:
    """
    Attributes:
        as_of (Union[Unset, str]):
        fresh (Union[Unset, bool]):
        attribution (Union[Unset, ExchangeRatesViewProviderAttribution]):
    """

    as_of: Union[Unset, str] = UNSET
    fresh: Union[Unset, bool] = UNSET
    attribution: Union[Unset, "ExchangeRatesViewProviderAttribution"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        as_of = self.as_of

        fresh = self.fresh

        attribution: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attribution, Unset):
            attribution = self.attribution.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if fresh is not UNSET:
            field_dict["fresh"] = fresh
        if attribution is not UNSET:
            field_dict["attribution"] = attribution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exchange_rates_view_provider_attribution import (
            ExchangeRatesViewProviderAttribution,
        )

        d = src_dict.copy()
        as_of = d.pop("asOf", UNSET)

        fresh = d.pop("fresh", UNSET)

        _attribution = d.pop("attribution", UNSET)
        attribution: Union[Unset, ExchangeRatesViewProviderAttribution]
        if isinstance(_attribution, Unset):
            attribution = UNSET
        else:
            attribution = ExchangeRatesViewProviderAttribution.from_dict(_attribution)

        exchange_rates_view_provider = cls(
            as_of=as_of,
            fresh=fresh,
            attribution=attribution,
        )

        exchange_rates_view_provider.additional_properties = d
        return exchange_rates_view_provider

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
