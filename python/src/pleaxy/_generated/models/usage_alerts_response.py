from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sensitivity_preset import SensitivityPreset
    from ..models.usage_alert_currency import UsageAlertCurrency
    from ..models.usage_alert_settings import UsageAlertSettings
    from ..models.usage_alert_view import UsageAlertView


T = TypeVar("T", bound="UsageAlertsResponse")


@_attrs_define
class UsageAlertsResponse:
    """
    Attributes:
        period (Union[Unset, str]):
        settings (Union[Unset, UsageAlertSettings]):
        preset (Union[Unset, SensitivityPreset]):
        currencies (Union[Unset, List['UsageAlertCurrency']]):
        alerts (Union[Unset, List['UsageAlertView']]):
        generated_at (Union[Unset, str]):
    """

    period: Union[Unset, str] = UNSET
    settings: Union[Unset, "UsageAlertSettings"] = UNSET
    preset: Union[Unset, "SensitivityPreset"] = UNSET
    currencies: Union[Unset, List["UsageAlertCurrency"]] = UNSET
    alerts: Union[Unset, List["UsageAlertView"]] = UNSET
    generated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        preset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset.to_dict()

        currencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        alerts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = alerts_item_data.to_dict()
                alerts.append(alerts_item)

        generated_at = self.generated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if settings is not UNSET:
            field_dict["settings"] = settings
        if preset is not UNSET:
            field_dict["preset"] = preset
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if generated_at is not UNSET:
            field_dict["generatedAt"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sensitivity_preset import SensitivityPreset
        from ..models.usage_alert_currency import UsageAlertCurrency
        from ..models.usage_alert_settings import UsageAlertSettings
        from ..models.usage_alert_view import UsageAlertView

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, UsageAlertSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = UsageAlertSettings.from_dict(_settings)

        _preset = d.pop("preset", UNSET)
        preset: Union[Unset, SensitivityPreset]
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = SensitivityPreset.from_dict(_preset)

        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = UsageAlertCurrency.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        alerts = []
        _alerts = d.pop("alerts", UNSET)
        for alerts_item_data in _alerts or []:
            alerts_item = UsageAlertView.from_dict(alerts_item_data)

            alerts.append(alerts_item)

        generated_at = d.pop("generatedAt", UNSET)

        usage_alerts_response = cls(
            period=period,
            settings=settings,
            preset=preset,
            currencies=currencies,
            alerts=alerts,
            generated_at=generated_at,
        )

        usage_alerts_response.additional_properties = d
        return usage_alerts_response

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
