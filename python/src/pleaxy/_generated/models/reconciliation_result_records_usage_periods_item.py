from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationResultRecordsUsagePeriodsItem")


@_attrs_define
class ReconciliationResultRecordsUsagePeriodsItem:
    """
    Attributes:
        invoice_line (Union[Unset, float]):
        period (Union[Unset, str]):
    """

    invoice_line: Union[Unset, float] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_line = self.invoice_line

        period = self.period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_line is not UNSET:
            field_dict["invoice_line"] = invoice_line
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_line = d.pop("invoice_line", UNSET)

        period = d.pop("period", UNSET)

        reconciliation_result_records_usage_periods_item = cls(
            invoice_line=invoice_line,
            period=period,
        )

        reconciliation_result_records_usage_periods_item.additional_properties = d
        return reconciliation_result_records_usage_periods_item

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
