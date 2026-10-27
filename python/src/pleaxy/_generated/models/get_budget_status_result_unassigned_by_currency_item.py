from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBudgetStatusResultUnassignedByCurrencyItem")


@_attrs_define
class GetBudgetStatusResultUnassignedByCurrencyItem:
    """
    Attributes:
        committed (Union[Unset, float]):
        actual (Union[Unset, float]):
        pending (Union[Unset, float]):
        unconverted (Union[Unset, float]):
        currency (Union[Unset, str]):
    """

    committed: Union[Unset, float] = UNSET
    actual: Union[Unset, float] = UNSET
    pending: Union[Unset, float] = UNSET
    unconverted: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        committed = self.committed

        actual = self.actual

        pending = self.pending

        unconverted = self.unconverted

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if committed is not UNSET:
            field_dict["committed"] = committed
        if actual is not UNSET:
            field_dict["actual"] = actual
        if pending is not UNSET:
            field_dict["pending"] = pending
        if unconverted is not UNSET:
            field_dict["unconverted"] = unconverted
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        committed = d.pop("committed", UNSET)

        actual = d.pop("actual", UNSET)

        pending = d.pop("pending", UNSET)

        unconverted = d.pop("unconverted", UNSET)

        currency = d.pop("currency", UNSET)

        get_budget_status_result_unassigned_by_currency_item = cls(
            committed=committed,
            actual=actual,
            pending=pending,
            unconverted=unconverted,
            currency=currency,
        )

        get_budget_status_result_unassigned_by_currency_item.additional_properties = d
        return get_budget_status_result_unassigned_by_currency_item

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
