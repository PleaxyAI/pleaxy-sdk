from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_deduction_input_kind import (
    InvoiceDeductionInputKind,
    check_invoice_deduction_input_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceDeductionInput")


@_attrs_define
class InvoiceDeductionInput:
    """
    Attributes:
        kind (InvoiceDeductionInputKind): prepayment: the buyer already paid it (a deposit, an advance). credit: the
            seller applied a credit it holds (prepaid or promotional credits).
        description (str): What it is, e.g. "30% deposit" or "AWS promotional credit". 1–200 characters.
        amount (float): More than 0, in the invoice's currency, including tax. With the withholdings, less than the
            invoice total.
        source_invoice_id (Union[Unset, str]): Prepayment only: the paid Pleaxy invoice it was - a deposit on the same
            purchase order from the same supplier. Its payment reference and date are filled in, and the purchase order
            isn't drawn twice for it.
        reference (Union[Unset, str]): The payment's reference, or the seller's id for the credit. 1–64 characters. A
            prepayment needs this or sourceInvoiceId.
        paid_on (Union[Unset, str]): Prepayment only: when it was paid, YYYY-MM-DD.
    """

    kind: InvoiceDeductionInputKind
    description: str
    amount: float
    source_invoice_id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    paid_on: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: str = self.kind

        description = self.description

        amount = self.amount

        source_invoice_id = self.source_invoice_id

        reference = self.reference

        paid_on = self.paid_on

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "description": description,
                "amount": amount,
            }
        )
        if source_invoice_id is not UNSET:
            field_dict["sourceInvoiceId"] = source_invoice_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if paid_on is not UNSET:
            field_dict["paidOn"] = paid_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = check_invoice_deduction_input_kind(d.pop("kind"))

        description = d.pop("description")

        amount = d.pop("amount")

        source_invoice_id = d.pop("sourceInvoiceId", UNSET)

        reference = d.pop("reference", UNSET)

        paid_on = d.pop("paidOn", UNSET)

        invoice_deduction_input = cls(
            kind=kind,
            description=description,
            amount=amount,
            source_invoice_id=source_invoice_id,
            reference=reference,
            paid_on=paid_on,
        )

        invoice_deduction_input.additional_properties = d
        return invoice_deduction_input

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
