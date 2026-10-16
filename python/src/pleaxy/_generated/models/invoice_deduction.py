from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_deduction_kind import (
    InvoiceDeductionKind,
    check_invoice_deduction_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceDeduction")


@_attrs_define
class InvoiceDeduction:
    """
    Attributes:
        kind (Union[Unset, InvoiceDeductionKind]):
        description (Union[Unset, str]):
        amount (Union[Unset, float]):
        source_invoice_id (Union[Unset, str]):
        reference (Union[Unset, str]):
        paid_on (Union[Unset, str]):
        stated (Union[Unset, bool]):
    """

    kind: Union[Unset, InvoiceDeductionKind] = UNSET
    description: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    source_invoice_id: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    paid_on: Union[Unset, str] = UNSET
    stated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        description = self.description

        amount = self.amount

        source_invoice_id = self.source_invoice_id

        reference = self.reference

        paid_on = self.paid_on

        stated = self.stated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if source_invoice_id is not UNSET:
            field_dict["sourceInvoiceId"] = source_invoice_id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if paid_on is not UNSET:
            field_dict["paidOn"] = paid_on
        if stated is not UNSET:
            field_dict["stated"] = stated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, InvoiceDeductionKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_invoice_deduction_kind(_kind)

        description = d.pop("description", UNSET)

        amount = d.pop("amount", UNSET)

        source_invoice_id = d.pop("sourceInvoiceId", UNSET)

        reference = d.pop("reference", UNSET)

        paid_on = d.pop("paidOn", UNSET)

        stated = d.pop("stated", UNSET)

        invoice_deduction = cls(
            kind=kind,
            description=description,
            amount=amount,
            source_invoice_id=source_invoice_id,
            reference=reference,
            paid_on=paid_on,
            stated=stated,
        )

        invoice_deduction.additional_properties = d
        return invoice_deduction

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
