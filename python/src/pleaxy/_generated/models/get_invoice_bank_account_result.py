from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_invoice_bank_account_result_hold import (
    GetInvoiceBankAccountResultHold,
    check_get_invoice_bank_account_result_hold,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_bank_account import SupplierBankAccount


T = TypeVar("T", bound="GetInvoiceBankAccountResult")


@_attrs_define
class GetInvoiceBankAccountResult:
    """
    Attributes:
        hold (Union[Unset, GetInvoiceBankAccountResultHold]):
        account (Union[Unset, SupplierBankAccount]):
        supplier_key (Union[Unset, str]):
    """

    hold: Union[Unset, GetInvoiceBankAccountResultHold] = UNSET
    account: Union[Unset, "SupplierBankAccount"] = UNSET
    supplier_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hold: Union[Unset, str] = UNSET
        if not isinstance(self.hold, Unset):
            hold = self.hold

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        supplier_key = self.supplier_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hold is not UNSET:
            field_dict["hold"] = hold
        if account is not UNSET:
            field_dict["account"] = account
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.supplier_bank_account import SupplierBankAccount

        d = src_dict.copy()
        _hold = d.pop("hold", UNSET)
        hold: Union[Unset, GetInvoiceBankAccountResultHold]
        if isinstance(_hold, Unset):
            hold = UNSET
        else:
            hold = check_get_invoice_bank_account_result_hold(_hold)

        _account = d.pop("account", UNSET)
        account: Union[Unset, SupplierBankAccount]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = SupplierBankAccount.from_dict(_account)

        supplier_key = d.pop("supplierKey", UNSET)

        get_invoice_bank_account_result = cls(
            hold=hold,
            account=account,
            supplier_key=supplier_key,
        )

        get_invoice_bank_account_result.additional_properties = d
        return get_invoice_bank_account_result

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
