from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remittance_instructions_method import (
    RemittanceInstructionsMethod,
    check_remittance_instructions_method,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemittanceInstructions")


@_attrs_define
class RemittanceInstructions:
    """
    Attributes:
        method (Union[Unset, RemittanceInstructionsMethod]):
        payee_name (Union[Unset, str]):
        bank_name (Union[Unset, str]):
        iban (Union[Unset, str]):
        account_number (Union[Unset, str]):
        bic (Union[Unset, str]):
        routing_number (Union[Unset, str]):
        mailing_address (Union[Unset, str]):
        payment_reference (Union[Unset, str]):
        notes (Union[Unset, str]):
    """

    method: Union[Unset, RemittanceInstructionsMethod] = UNSET
    payee_name: Union[Unset, str] = UNSET
    bank_name: Union[Unset, str] = UNSET
    iban: Union[Unset, str] = UNSET
    account_number: Union[Unset, str] = UNSET
    bic: Union[Unset, str] = UNSET
    routing_number: Union[Unset, str] = UNSET
    mailing_address: Union[Unset, str] = UNSET
    payment_reference: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        payee_name = self.payee_name

        bank_name = self.bank_name

        iban = self.iban

        account_number = self.account_number

        bic = self.bic

        routing_number = self.routing_number

        mailing_address = self.mailing_address

        payment_reference = self.payment_reference

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if payee_name is not UNSET:
            field_dict["payeeName"] = payee_name
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if iban is not UNSET:
            field_dict["iban"] = iban
        if account_number is not UNSET:
            field_dict["accountNumber"] = account_number
        if bic is not UNSET:
            field_dict["bic"] = bic
        if routing_number is not UNSET:
            field_dict["routingNumber"] = routing_number
        if mailing_address is not UNSET:
            field_dict["mailingAddress"] = mailing_address
        if payment_reference is not UNSET:
            field_dict["paymentReference"] = payment_reference
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, RemittanceInstructionsMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_remittance_instructions_method(_method)

        payee_name = d.pop("payeeName", UNSET)

        bank_name = d.pop("bankName", UNSET)

        iban = d.pop("iban", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        bic = d.pop("bic", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        mailing_address = d.pop("mailingAddress", UNSET)

        payment_reference = d.pop("paymentReference", UNSET)

        notes = d.pop("notes", UNSET)

        remittance_instructions = cls(
            method=method,
            payee_name=payee_name,
            bank_name=bank_name,
            iban=iban,
            account_number=account_number,
            bic=bic,
            routing_number=routing_number,
            mailing_address=mailing_address,
            payment_reference=payment_reference,
            notes=notes,
        )

        remittance_instructions.additional_properties = d
        return remittance_instructions

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
