from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_control_settings import BudgetControlSettings
    from ..models.budget_period import BudgetPeriod
    from ..models.budget_status import BudgetStatus
    from ..models.get_budget_status_result_unassigned_by_currency_item import (
        GetBudgetStatusResultUnassignedByCurrencyItem,
    )
    from ..models.spend_figures import SpendFigures


T = TypeVar("T", bound="GetBudgetStatusResult")


@_attrs_define
class GetBudgetStatusResult:
    """
    Attributes:
        settings (Union[Unset, BudgetControlSettings]):
        period (Union[Unset, BudgetPeriod]):
        currency (Union[Unset, str]):
        cost_centers (Union[Unset, List['BudgetStatus']]):
        unassigned (Union[Unset, SpendFigures]):
        unassigned_by_currency (Union[Unset, List['GetBudgetStatusResultUnassignedByCurrencyItem']]):
    """

    settings: Union[Unset, "BudgetControlSettings"] = UNSET
    period: Union[Unset, "BudgetPeriod"] = UNSET
    currency: Union[Unset, str] = UNSET
    cost_centers: Union[Unset, List["BudgetStatus"]] = UNSET
    unassigned: Union[Unset, "SpendFigures"] = UNSET
    unassigned_by_currency: Union[
        Unset, List["GetBudgetStatusResultUnassignedByCurrencyItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        currency = self.currency

        cost_centers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cost_centers, Unset):
            cost_centers = []
            for cost_centers_item_data in self.cost_centers:
                cost_centers_item = cost_centers_item_data.to_dict()
                cost_centers.append(cost_centers_item)

        unassigned: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unassigned, Unset):
            unassigned = self.unassigned.to_dict()

        unassigned_by_currency: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unassigned_by_currency, Unset):
            unassigned_by_currency = []
            for unassigned_by_currency_item_data in self.unassigned_by_currency:
                unassigned_by_currency_item = unassigned_by_currency_item_data.to_dict()
                unassigned_by_currency.append(unassigned_by_currency_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if period is not UNSET:
            field_dict["period"] = period
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cost_centers is not UNSET:
            field_dict["costCenters"] = cost_centers
        if unassigned is not UNSET:
            field_dict["unassigned"] = unassigned
        if unassigned_by_currency is not UNSET:
            field_dict["unassignedByCurrency"] = unassigned_by_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.budget_control_settings import BudgetControlSettings
        from ..models.budget_period import BudgetPeriod
        from ..models.budget_status import BudgetStatus
        from ..models.get_budget_status_result_unassigned_by_currency_item import (
            GetBudgetStatusResultUnassignedByCurrencyItem,
        )
        from ..models.spend_figures import SpendFigures

        d = src_dict.copy()
        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, BudgetControlSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = BudgetControlSettings.from_dict(_settings)

        _period = d.pop("period", UNSET)
        period: Union[Unset, BudgetPeriod]
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = BudgetPeriod.from_dict(_period)

        currency = d.pop("currency", UNSET)

        cost_centers = []
        _cost_centers = d.pop("costCenters", UNSET)
        for cost_centers_item_data in _cost_centers or []:
            cost_centers_item = BudgetStatus.from_dict(cost_centers_item_data)

            cost_centers.append(cost_centers_item)

        _unassigned = d.pop("unassigned", UNSET)
        unassigned: Union[Unset, SpendFigures]
        if isinstance(_unassigned, Unset):
            unassigned = UNSET
        else:
            unassigned = SpendFigures.from_dict(_unassigned)

        unassigned_by_currency = []
        _unassigned_by_currency = d.pop("unassignedByCurrency", UNSET)
        for unassigned_by_currency_item_data in _unassigned_by_currency or []:
            unassigned_by_currency_item = (
                GetBudgetStatusResultUnassignedByCurrencyItem.from_dict(
                    unassigned_by_currency_item_data
                )
            )

            unassigned_by_currency.append(unassigned_by_currency_item)

        get_budget_status_result = cls(
            settings=settings,
            period=period,
            currency=currency,
            cost_centers=cost_centers,
            unassigned=unassigned,
            unassigned_by_currency=unassigned_by_currency,
        )

        get_budget_status_result.additional_properties = d
        return get_budget_status_result

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
