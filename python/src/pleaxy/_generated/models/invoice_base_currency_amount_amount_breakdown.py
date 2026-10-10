from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_breakdown_group import InvoiceBreakdownGroup


T = TypeVar("T", bound="InvoiceBaseCurrencyAmountAmountBreakdown")


@_attrs_define
class InvoiceBaseCurrencyAmountAmountBreakdown:
    """
    Attributes:
        sub_total_amount (Union[Unset, float]):
        discounts (Union[Unset, InvoiceBreakdownGroup]):
        fees (Union[Unset, InvoiceBreakdownGroup]):
        taxes (Union[Unset, InvoiceBreakdownGroup]):
    """

    sub_total_amount: Union[Unset, float] = UNSET
    discounts: Union[Unset, "InvoiceBreakdownGroup"] = UNSET
    fees: Union[Unset, "InvoiceBreakdownGroup"] = UNSET
    taxes: Union[Unset, "InvoiceBreakdownGroup"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_total_amount = self.sub_total_amount

        discounts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = self.discounts.to_dict()

        fees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        taxes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = self.taxes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_total_amount is not UNSET:
            field_dict["subTotalAmount"] = sub_total_amount
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if fees is not UNSET:
            field_dict["fees"] = fees
        if taxes is not UNSET:
            field_dict["taxes"] = taxes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_breakdown_group import InvoiceBreakdownGroup

        d = src_dict.copy()
        sub_total_amount = d.pop("subTotalAmount", UNSET)

        _discounts = d.pop("discounts", UNSET)
        discounts: Union[Unset, InvoiceBreakdownGroup]
        if isinstance(_discounts, Unset):
            discounts = UNSET
        else:
            discounts = InvoiceBreakdownGroup.from_dict(_discounts)

        _fees = d.pop("fees", UNSET)
        fees: Union[Unset, InvoiceBreakdownGroup]
        if isinstance(_fees, Unset):
            fees = UNSET
        else:
            fees = InvoiceBreakdownGroup.from_dict(_fees)

        _taxes = d.pop("taxes", UNSET)
        taxes: Union[Unset, InvoiceBreakdownGroup]
        if isinstance(_taxes, Unset):
            taxes = UNSET
        else:
            taxes = InvoiceBreakdownGroup.from_dict(_taxes)

        invoice_base_currency_amount_amount_breakdown = cls(
            sub_total_amount=sub_total_amount,
            discounts=discounts,
            fees=fees,
            taxes=taxes,
        )

        invoice_base_currency_amount_amount_breakdown.additional_properties = d
        return invoice_base_currency_amount_amount_breakdown

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
