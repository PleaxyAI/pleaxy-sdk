from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reconciliation_failure_check import (
    ReconciliationFailureCheck,
    check_reconciliation_failure_check,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReconciliationFailure")


@_attrs_define
class ReconciliationFailure:
    """
    Attributes:
        check (Union[Unset, ReconciliationFailureCheck]):
        code (Union[Unset, str]):
        invoice_line (Union[Unset, float]):
        order_line (Union[Unset, float]):
        agreement_id (Union[Unset, str]):
        agreement_version (Union[Unset, float]):
        allowed (Union[Unset, str]):
        billed (Union[Unset, str]):
    """

    check: Union[Unset, ReconciliationFailureCheck] = UNSET
    code: Union[Unset, str] = UNSET
    invoice_line: Union[Unset, float] = UNSET
    order_line: Union[Unset, float] = UNSET
    agreement_id: Union[Unset, str] = UNSET
    agreement_version: Union[Unset, float] = UNSET
    allowed: Union[Unset, str] = UNSET
    billed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        check: Union[Unset, str] = UNSET
        if not isinstance(self.check, Unset):
            check = self.check

        code = self.code

        invoice_line = self.invoice_line

        order_line = self.order_line

        agreement_id = self.agreement_id

        agreement_version = self.agreement_version

        allowed = self.allowed

        billed = self.billed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check is not UNSET:
            field_dict["check"] = check
        if code is not UNSET:
            field_dict["code"] = code
        if invoice_line is not UNSET:
            field_dict["invoice_line"] = invoice_line
        if order_line is not UNSET:
            field_dict["order_line"] = order_line
        if agreement_id is not UNSET:
            field_dict["agreement_id"] = agreement_id
        if agreement_version is not UNSET:
            field_dict["agreement_version"] = agreement_version
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if billed is not UNSET:
            field_dict["billed"] = billed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _check = d.pop("check", UNSET)
        check: Union[Unset, ReconciliationFailureCheck]
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = check_reconciliation_failure_check(_check)

        code = d.pop("code", UNSET)

        invoice_line = d.pop("invoice_line", UNSET)

        order_line = d.pop("order_line", UNSET)

        agreement_id = d.pop("agreement_id", UNSET)

        agreement_version = d.pop("agreement_version", UNSET)

        allowed = d.pop("allowed", UNSET)

        billed = d.pop("billed", UNSET)

        reconciliation_failure = cls(
            check=check,
            code=code,
            invoice_line=invoice_line,
            order_line=order_line,
            agreement_id=agreement_id,
            agreement_version=agreement_version,
            allowed=allowed,
            billed=billed,
        )

        reconciliation_failure.additional_properties = d
        return reconciliation_failure

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
