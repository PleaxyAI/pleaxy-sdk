from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetCheckInput")


@_attrs_define
class BudgetCheckInput:
    """
    Attributes:
        amount (float): The document's amount, in `currency`.
        currency (str): ISO 4217 currency of `amount`.
        cost_center (Union[Unset, str]): The cost center code (or name) the document books to. Without one there is
            nothing to check (no_budget).
        exclude_order_id (Union[Unset, str]): An existing order being edited, so it doesn't count against itself.
        blanket (Union[Unset, bool]): A blanket order (billed as used, up to `amount`): what is checked is
            `expectedMonthly` for the current period's months within its term, never `amount`.
        expected_monthly (Union[Unset, float]): With blanket: what the order is expected to bill each month, in
            `currency`.
        valid_until (Union[Unset, str]): With blanket: the last day it runs (YYYY-MM-DD), its lines' latest validUntil;
            open-ended when absent.
    """

    amount: float
    currency: str
    cost_center: Union[Unset, str] = UNSET
    exclude_order_id: Union[Unset, str] = UNSET
    blanket: Union[Unset, bool] = UNSET
    expected_monthly: Union[Unset, float] = UNSET
    valid_until: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        currency = self.currency

        cost_center = self.cost_center

        exclude_order_id = self.exclude_order_id

        blanket = self.blanket

        expected_monthly = self.expected_monthly

        valid_until = self.valid_until

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if exclude_order_id is not UNSET:
            field_dict["excludeOrderId"] = exclude_order_id
        if blanket is not UNSET:
            field_dict["blanket"] = blanket
        if expected_monthly is not UNSET:
            field_dict["expectedMonthly"] = expected_monthly
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        currency = d.pop("currency")

        cost_center = d.pop("costCenter", UNSET)

        exclude_order_id = d.pop("excludeOrderId", UNSET)

        blanket = d.pop("blanket", UNSET)

        expected_monthly = d.pop("expectedMonthly", UNSET)

        valid_until = d.pop("validUntil", UNSET)

        budget_check_input = cls(
            amount=amount,
            currency=currency,
            cost_center=cost_center,
            exclude_order_id=exclude_order_id,
            blanket=blanket,
            expected_monthly=expected_monthly,
            valid_until=valid_until,
        )

        budget_check_input.additional_properties = d
        return budget_check_input

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
