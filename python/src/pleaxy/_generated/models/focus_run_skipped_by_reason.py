from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusRunSkippedByReason")


@_attrs_define
class FocusRunSkippedByReason:
    """
    Attributes:
        no_billing_period (Union[Unset, float]):
        bad_number (Union[Unset, float]):
        bad_currency (Union[Unset, float]):
        bad_charge_period (Union[Unset, float]):
    """

    no_billing_period: Union[Unset, float] = UNSET
    bad_number: Union[Unset, float] = UNSET
    bad_currency: Union[Unset, float] = UNSET
    bad_charge_period: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        no_billing_period = self.no_billing_period

        bad_number = self.bad_number

        bad_currency = self.bad_currency

        bad_charge_period = self.bad_charge_period

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_billing_period is not UNSET:
            field_dict["noBillingPeriod"] = no_billing_period
        if bad_number is not UNSET:
            field_dict["badNumber"] = bad_number
        if bad_currency is not UNSET:
            field_dict["badCurrency"] = bad_currency
        if bad_charge_period is not UNSET:
            field_dict["badChargePeriod"] = bad_charge_period

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        no_billing_period = d.pop("noBillingPeriod", UNSET)

        bad_number = d.pop("badNumber", UNSET)

        bad_currency = d.pop("badCurrency", UNSET)

        bad_charge_period = d.pop("badChargePeriod", UNSET)

        focus_run_skipped_by_reason = cls(
            no_billing_period=no_billing_period,
            bad_number=bad_number,
            bad_currency=bad_currency,
            bad_charge_period=bad_charge_period,
        )

        focus_run_skipped_by_reason.additional_properties = d
        return focus_run_skipped_by_reason

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
