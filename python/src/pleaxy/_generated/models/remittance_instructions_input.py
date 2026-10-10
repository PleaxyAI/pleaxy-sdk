from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remittance_instructions_input_method import (
    RemittanceInstructionsInputMethod,
    check_remittance_instructions_input_method,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemittanceInstructionsInput")


@_attrs_define
class RemittanceInstructionsInput:
    """
    Attributes:
        method (RemittanceInstructionsInputMethod): bank_transfer needs iban or accountNumber. wire needs iban or
            accountNumber, plus bic or routingNumber. ach needs accountNumber and a 9-digit ABA routingNumber. check needs
            mailingAddress. other needs notes.
        payee_name (str): The account holder, or the payee on a check. 1–140 characters.
        bank_name (Union[Unset, str]): At most 140 characters
        iban (Union[Unset, str]): Spaces allowed; stored uppercase without them. Must pass the IBAN check digits.
        account_number (Union[Unset, str]): Letters, digits, spaces and '-', at most 34 characters
        bic (Union[Unset, str]): SWIFT/BIC, 8 or 11 characters
        routing_number (Union[Unset, str]): ABA routing number, sort code, BSB or similar: digits, spaces and '-', at
            most 20 characters
        mailing_address (Union[Unset, str]): Where to mail a check. At most 300 characters.
        payment_reference (Union[Unset, str]): What the buyer should quote with the payment. At most 140 characters.
        notes (Union[Unset, str]): Anything else the buyer needs to pay. At most 500 characters.
    """

    method: RemittanceInstructionsInputMethod
    payee_name: str
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
        method: str = self.method

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
        field_dict.update(
            {
                "method": method,
                "payeeName": payee_name,
            }
        )
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
        method = check_remittance_instructions_input_method(d.pop("method"))

        payee_name = d.pop("payeeName")

        bank_name = d.pop("bankName", UNSET)

        iban = d.pop("iban", UNSET)

        account_number = d.pop("accountNumber", UNSET)

        bic = d.pop("bic", UNSET)

        routing_number = d.pop("routingNumber", UNSET)

        mailing_address = d.pop("mailingAddress", UNSET)

        payment_reference = d.pop("paymentReference", UNSET)

        notes = d.pop("notes", UNSET)

        remittance_instructions_input = cls(
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

        remittance_instructions_input.additional_properties = d
        return remittance_instructions_input

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
