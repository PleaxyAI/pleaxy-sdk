from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reject_invoice_input_reason_code import (
    RejectInvoiceInputReasonCode,
    check_reject_invoice_input_reason_code,
)

T = TypeVar("T", bound="RejectInvoiceInput")


@_attrs_define
class RejectInvoiceInput:
    """
    Attributes:
        reason_code (RejectInvoiceInputReasonCode):
        reason (str): Shown to the supplier exactly as written, as plain text. Line breaks, control and invisible
            characters are removed; the minimum counts letters and numbers.
    """

    reason_code: RejectInvoiceInputReasonCode
    reason: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason_code: str = self.reason_code

        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reasonCode": reason_code,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reason_code = check_reject_invoice_input_reason_code(d.pop("reasonCode"))

        reason = d.pop("reason")

        reject_invoice_input = cls(
            reason_code=reason_code,
            reason=reason,
        )

        reject_invoice_input.additional_properties = d
        return reject_invoice_input

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
