from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.supplier_bank_account_approval_verification import (
    SupplierBankAccountApprovalVerification,
    check_supplier_bank_account_approval_verification,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bank_check import BankCheck
    from ..models.supplier_bank_account_approval_by import SupplierBankAccountApprovalBy


T = TypeVar("T", bound="SupplierBankAccountApproval")


@_attrs_define
class SupplierBankAccountApproval:
    """
    Attributes:
        verification (Union[Unset, SupplierBankAccountApprovalVerification]):
        at (Union[Unset, str]):
        by (Union[Unset, SupplierBankAccountApprovalBy]):
        check (Union[Unset, BankCheck]):
        invoice_id (Union[Unset, str]):
    """

    verification: Union[Unset, SupplierBankAccountApprovalVerification] = UNSET
    at: Union[Unset, str] = UNSET
    by: Union[Unset, "SupplierBankAccountApprovalBy"] = UNSET
    check: Union[Unset, "BankCheck"] = UNSET
    invoice_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verification: Union[Unset, str] = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification

        at = self.at

        by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by, Unset):
            by = self.by.to_dict()

        check: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.check, Unset):
            check = self.check.to_dict()

        invoice_id = self.invoice_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verification is not UNSET:
            field_dict["verification"] = verification
        if at is not UNSET:
            field_dict["at"] = at
        if by is not UNSET:
            field_dict["by"] = by
        if check is not UNSET:
            field_dict["check"] = check
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bank_check import BankCheck
        from ..models.supplier_bank_account_approval_by import (
            SupplierBankAccountApprovalBy,
        )

        d = src_dict.copy()
        _verification = d.pop("verification", UNSET)
        verification: Union[Unset, SupplierBankAccountApprovalVerification]
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = check_supplier_bank_account_approval_verification(
                _verification
            )

        at = d.pop("at", UNSET)

        _by = d.pop("by", UNSET)
        by: Union[Unset, SupplierBankAccountApprovalBy]
        if isinstance(_by, Unset):
            by = UNSET
        else:
            by = SupplierBankAccountApprovalBy.from_dict(_by)

        _check = d.pop("check", UNSET)
        check: Union[Unset, BankCheck]
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = BankCheck.from_dict(_check)

        invoice_id = d.pop("invoiceId", UNSET)

        supplier_bank_account_approval = cls(
            verification=verification,
            at=at,
            by=by,
            check=check,
            invoice_id=invoice_id,
        )

        supplier_bank_account_approval.additional_properties = d
        return supplier_bank_account_approval

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
