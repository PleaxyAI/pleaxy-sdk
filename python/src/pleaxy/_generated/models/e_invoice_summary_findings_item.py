from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_invoice_summary_findings_item_severity import (
    EInvoiceSummaryFindingsItemSeverity,
    check_e_invoice_summary_findings_item_severity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EInvoiceSummaryFindingsItem")


@_attrs_define
class EInvoiceSummaryFindingsItem:
    """
    Attributes:
        rule (Union[Unset, str]):
        severity (Union[Unset, EInvoiceSummaryFindingsItemSeverity]):
        position (Union[Unset, float]):
    """

    rule: Union[Unset, str] = UNSET
    severity: Union[Unset, EInvoiceSummaryFindingsItemSeverity] = UNSET
    position: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule = self.rule

        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule is not UNSET:
            field_dict["rule"] = rule
        if severity is not UNSET:
            field_dict["severity"] = severity
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rule = d.pop("rule", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, EInvoiceSummaryFindingsItemSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_e_invoice_summary_findings_item_severity(_severity)

        position = d.pop("position", UNSET)

        e_invoice_summary_findings_item = cls(
            rule=rule,
            severity=severity,
            position=position,
        )

        e_invoice_summary_findings_item.additional_properties = d
        return e_invoice_summary_findings_item

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
