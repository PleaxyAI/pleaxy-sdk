from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_rejection_reason_code import (
    InvoiceRejectionReasonCode,
    check_invoice_rejection_reason_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceRejection")


@_attrs_define
class InvoiceRejection:
    """
    Attributes:
        reason_code (Union[Unset, InvoiceRejectionReasonCode]):
        reason (Union[Unset, str]):
        at (Union[Unset, str]):
    """

    reason_code: Union[Unset, InvoiceRejectionReasonCode] = UNSET
    reason: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason_code: Union[Unset, str] = UNSET
        if not isinstance(self.reason_code, Unset):
            reason_code = self.reason_code

        reason = self.reason

        at = self.at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if at is not UNSET:
            field_dict["at"] = at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _reason_code = d.pop("reasonCode", UNSET)
        reason_code: Union[Unset, InvoiceRejectionReasonCode]
        if isinstance(_reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = check_invoice_rejection_reason_code(_reason_code)

        reason = d.pop("reason", UNSET)

        at = d.pop("at", UNSET)

        invoice_rejection = cls(
            reason_code=reason_code,
            reason=reason,
            at=at,
        )

        invoice_rejection.additional_properties = d
        return invoice_rejection

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
