from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exchange_rate_row import ExchangeRateRow
    from ..models.exchange_rates_view_provider import ExchangeRatesViewProvider


T = TypeVar("T", bound="ExchangeRatesView")


@_attrs_define
class ExchangeRatesView:
    """
    Attributes:
        workspace_currency (Union[Unset, str]):
        warning_pct (Union[Unset, float]):
        rows (Union[Unset, List['ExchangeRateRow']]):
        provider (Union[Unset, ExchangeRatesViewProvider]):
    """

    workspace_currency: Union[Unset, str] = UNSET
    warning_pct: Union[Unset, float] = UNSET
    rows: Union[Unset, List["ExchangeRateRow"]] = UNSET
    provider: Union[Unset, "ExchangeRatesViewProvider"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace_currency = self.workspace_currency

        warning_pct = self.warning_pct

        rows: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace_currency is not UNSET:
            field_dict["workspaceCurrency"] = workspace_currency
        if warning_pct is not UNSET:
            field_dict["warningPct"] = warning_pct
        if rows is not UNSET:
            field_dict["rows"] = rows
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.exchange_rate_row import ExchangeRateRow
        from ..models.exchange_rates_view_provider import ExchangeRatesViewProvider

        d = src_dict.copy()
        workspace_currency = d.pop("workspaceCurrency", UNSET)

        warning_pct = d.pop("warningPct", UNSET)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = ExchangeRateRow.from_dict(rows_item_data)

            rows.append(rows_item)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, ExchangeRatesViewProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ExchangeRatesViewProvider.from_dict(_provider)

        exchange_rates_view = cls(
            workspace_currency=workspace_currency,
            warning_pct=warning_pct,
            rows=rows,
            provider=provider,
        )

        exchange_rates_view.additional_properties = d
        return exchange_rates_view

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
