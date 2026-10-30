from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiCostCentersResponseUnattributedItem")


@_attrs_define
class AiCostCentersResponseUnattributedItem:
    """
    Attributes:
        currency (Union[Unset, str]):
        month_to_date (Union[Unset, float]):
        forecast (Union[Unset, float]):
    """

    currency: Union[Unset, str] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        month_to_date = self.month_to_date

        forecast = self.forecast

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if forecast is not UNSET:
            field_dict["forecast"] = forecast

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        month_to_date = d.pop("monthToDate", UNSET)

        forecast = d.pop("forecast", UNSET)

        ai_cost_centers_response_unattributed_item = cls(
            currency=currency,
            month_to_date=month_to_date,
            forecast=forecast,
        )

        ai_cost_centers_response_unattributed_item.additional_properties = d
        return ai_cost_centers_response_unattributed_item

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
