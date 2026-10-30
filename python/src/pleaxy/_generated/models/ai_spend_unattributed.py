from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_meter_quantity import AiMeterQuantity


T = TypeVar("T", bound="AiSpendUnattributed")


@_attrs_define
class AiSpendUnattributed:
    """
    Attributes:
        currency (Union[Unset, str]):
        month_to_date (Union[Unset, float]):
        forecast (Union[Unset, float]):
        last_month (Union[Unset, float]):
        change_pct (Union[Unset, float]):
        quantities (Union[Unset, List['AiMeterQuantity']]):
    """

    currency: Union[Unset, str] = UNSET
    month_to_date: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    last_month: Union[Unset, float] = UNSET
    change_pct: Union[Unset, float] = UNSET
    quantities: Union[Unset, List["AiMeterQuantity"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency

        month_to_date = self.month_to_date

        forecast = self.forecast

        last_month = self.last_month

        change_pct = self.change_pct

        quantities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.quantities, Unset):
            quantities = []
            for quantities_item_data in self.quantities:
                quantities_item = quantities_item_data.to_dict()
                quantities.append(quantities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if month_to_date is not UNSET:
            field_dict["monthToDate"] = month_to_date
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if last_month is not UNSET:
            field_dict["lastMonth"] = last_month
        if change_pct is not UNSET:
            field_dict["changePct"] = change_pct
        if quantities is not UNSET:
            field_dict["quantities"] = quantities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_meter_quantity import AiMeterQuantity

        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        month_to_date = d.pop("monthToDate", UNSET)

        forecast = d.pop("forecast", UNSET)

        last_month = d.pop("lastMonth", UNSET)

        change_pct = d.pop("changePct", UNSET)

        quantities = []
        _quantities = d.pop("quantities", UNSET)
        for quantities_item_data in _quantities or []:
            quantities_item = AiMeterQuantity.from_dict(quantities_item_data)

            quantities.append(quantities_item)

        ai_spend_unattributed = cls(
            currency=currency,
            month_to_date=month_to_date,
            forecast=forecast,
            last_month=last_month,
            change_pct=change_pct,
            quantities=quantities,
        )

        ai_spend_unattributed.additional_properties = d
        return ai_spend_unattributed

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
