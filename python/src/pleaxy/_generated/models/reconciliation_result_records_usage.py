from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_result_records_usage_source import (
    ReconciliationResultRecordsUsageSource,
    check_reconciliation_result_records_usage_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconciliation_result_records_usage_periods_item import (
        ReconciliationResultRecordsUsagePeriodsItem,
    )


T = TypeVar("T", bound="ReconciliationResultRecordsUsage")


@_attrs_define
class ReconciliationResultRecordsUsage:
    """
    Attributes:
        source (Union[Unset, ReconciliationResultRecordsUsageSource]):
        amount (Union[Unset, str]):
        currency (Union[Unset, str]):
        periods (Union[Unset, List['ReconciliationResultRecordsUsagePeriodsItem']]):
    """

    source: Union[Unset, ReconciliationResultRecordsUsageSource] = UNSET
    amount: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    periods: Union[Unset, List["ReconciliationResultRecordsUsagePeriodsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        amount = self.amount

        currency = self.currency

        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reconciliation_result_records_usage_periods_item import (
            ReconciliationResultRecordsUsagePeriodsItem,
        )

        d = src_dict.copy()
        _source = d.pop("source", UNSET)
        source: Union[Unset, ReconciliationResultRecordsUsageSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_reconciliation_result_records_usage_source(_source)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = ReconciliationResultRecordsUsagePeriodsItem.from_dict(
                periods_item_data
            )

            periods.append(periods_item)

        reconciliation_result_records_usage = cls(
            source=source,
            amount=amount,
            currency=currency,
            periods=periods,
        )

        reconciliation_result_records_usage.additional_properties = d
        return reconciliation_result_records_usage

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
