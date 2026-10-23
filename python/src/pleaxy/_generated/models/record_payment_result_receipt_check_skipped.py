from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.record_payment_result_receipt_check_skipped_reason import (
    RecordPaymentResultReceiptCheckSkippedReason,
    check_record_payment_result_receipt_check_skipped_reason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_control_finding import InvoiceControlFinding


T = TypeVar("T", bound="RecordPaymentResultReceiptCheckSkipped")


@_attrs_define
class RecordPaymentResultReceiptCheckSkipped:
    """
    Attributes:
        reason (Union[Unset, RecordPaymentResultReceiptCheckSkippedReason]):
        at (Union[Unset, str]):
        findings (Union[Unset, List['InvoiceControlFinding']]):
    """

    reason: Union[Unset, RecordPaymentResultReceiptCheckSkippedReason] = UNSET
    at: Union[Unset, str] = UNSET
    findings: Union[Unset, List["InvoiceControlFinding"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        at = self.at

        findings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.findings, Unset):
            findings = []
            for findings_item_data in self.findings:
                findings_item = findings_item_data.to_dict()
                findings.append(findings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if at is not UNSET:
            field_dict["at"] = at
        if findings is not UNSET:
            field_dict["findings"] = findings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_control_finding import InvoiceControlFinding

        d = src_dict.copy()
        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, RecordPaymentResultReceiptCheckSkippedReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_record_payment_result_receipt_check_skipped_reason(_reason)

        at = d.pop("at", UNSET)

        findings = []
        _findings = d.pop("findings", UNSET)
        for findings_item_data in _findings or []:
            findings_item = InvoiceControlFinding.from_dict(findings_item_data)

            findings.append(findings_item)

        record_payment_result_receipt_check_skipped = cls(
            reason=reason,
            at=at,
            findings=findings,
        )

        record_payment_result_receipt_check_skipped.additional_properties = d
        return record_payment_result_receipt_check_skipped

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
