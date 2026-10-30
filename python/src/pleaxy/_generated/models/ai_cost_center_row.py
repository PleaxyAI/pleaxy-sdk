from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_cost_center_row_alert import AiCostCenterRowAlert


T = TypeVar("T", bound="AiCostCenterRow")


@_attrs_define
class AiCostCenterRow:
    """
    Attributes:
        cost_center (Union[Unset, str]):
        cost_center_name (Union[Unset, str]):
        currency (Union[Unset, str]):
        budget (Union[Unset, float]):
        committed (Union[Unset, float]):
        actual (Union[Unset, float]):
        accruing (Union[Unset, float]):
        forecast (Union[Unset, float]):
        pct_with_forecast (Union[Unset, float]):
        alert (Union[Unset, AiCostCenterRowAlert]):
    """

    cost_center: Union[Unset, str] = UNSET
    cost_center_name: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    budget: Union[Unset, float] = UNSET
    committed: Union[Unset, float] = UNSET
    actual: Union[Unset, float] = UNSET
    accruing: Union[Unset, float] = UNSET
    forecast: Union[Unset, float] = UNSET
    pct_with_forecast: Union[Unset, float] = UNSET
    alert: Union[Unset, "AiCostCenterRowAlert"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center = self.cost_center

        cost_center_name = self.cost_center_name

        currency = self.currency

        budget = self.budget

        committed = self.committed

        actual = self.actual

        accruing = self.accruing

        forecast = self.forecast

        pct_with_forecast = self.pct_with_forecast

        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if cost_center_name is not UNSET:
            field_dict["costCenterName"] = cost_center_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if budget is not UNSET:
            field_dict["budget"] = budget
        if committed is not UNSET:
            field_dict["committed"] = committed
        if actual is not UNSET:
            field_dict["actual"] = actual
        if accruing is not UNSET:
            field_dict["accruing"] = accruing
        if forecast is not UNSET:
            field_dict["forecast"] = forecast
        if pct_with_forecast is not UNSET:
            field_dict["pctWithForecast"] = pct_with_forecast
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_cost_center_row_alert import AiCostCenterRowAlert

        d = src_dict.copy()
        cost_center = d.pop("costCenter", UNSET)

        cost_center_name = d.pop("costCenterName", UNSET)

        currency = d.pop("currency", UNSET)

        budget = d.pop("budget", UNSET)

        committed = d.pop("committed", UNSET)

        actual = d.pop("actual", UNSET)

        accruing = d.pop("accruing", UNSET)

        forecast = d.pop("forecast", UNSET)

        pct_with_forecast = d.pop("pctWithForecast", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, AiCostCenterRowAlert]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AiCostCenterRowAlert.from_dict(_alert)

        ai_cost_center_row = cls(
            cost_center=cost_center,
            cost_center_name=cost_center_name,
            currency=currency,
            budget=budget,
            committed=committed,
            actual=actual,
            accruing=accruing,
            forecast=forecast,
            pct_with_forecast=pct_with_forecast,
            alert=alert,
        )

        ai_cost_center_row.additional_properties = d
        return ai_cost_center_row

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
