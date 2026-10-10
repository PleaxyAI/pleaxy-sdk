from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breakdown_group_input import BreakdownGroupInput


T = TypeVar("T", bound="AmountBreakdownInput")


@_attrs_define
class AmountBreakdownInput:
    """
    Attributes:
        sub_total_amount (Union[Unset, float]):
        discounts (Union[Unset, BreakdownGroupInput]):
        fees (Union[Unset, BreakdownGroupInput]):
        taxes (Union[Unset, BreakdownGroupInput]):
    """

    sub_total_amount: Union[Unset, float] = UNSET
    discounts: Union[Unset, "BreakdownGroupInput"] = UNSET
    fees: Union[Unset, "BreakdownGroupInput"] = UNSET
    taxes: Union[Unset, "BreakdownGroupInput"] = UNSET
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
        from ..models.breakdown_group_input import BreakdownGroupInput

        d = src_dict.copy()
        sub_total_amount = d.pop("subTotalAmount", UNSET)

        _discounts = d.pop("discounts", UNSET)
        discounts: Union[Unset, BreakdownGroupInput]
        if isinstance(_discounts, Unset):
            discounts = UNSET
        else:
            discounts = BreakdownGroupInput.from_dict(_discounts)

        _fees = d.pop("fees", UNSET)
        fees: Union[Unset, BreakdownGroupInput]
        if isinstance(_fees, Unset):
            fees = UNSET
        else:
            fees = BreakdownGroupInput.from_dict(_fees)

        _taxes = d.pop("taxes", UNSET)
        taxes: Union[Unset, BreakdownGroupInput]
        if isinstance(_taxes, Unset):
            taxes = UNSET
        else:
            taxes = BreakdownGroupInput.from_dict(_taxes)

        amount_breakdown_input = cls(
            sub_total_amount=sub_total_amount,
            discounts=discounts,
            fees=fees,
            taxes=taxes,
        )

        amount_breakdown_input.additional_properties = d
        return amount_breakdown_input

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
