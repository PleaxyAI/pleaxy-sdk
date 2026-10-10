from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_connection_billing_current_period_estimate_confidence import (
    CloudConnectionBillingCurrentPeriodEstimateConfidence,
    check_cloud_connection_billing_current_period_estimate_confidence,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudConnectionBillingCurrentPeriodEstimate")


@_attrs_define
class CloudConnectionBillingCurrentPeriodEstimate:
    """
    Attributes:
        total_amount (Union[Unset, float]):
        forecast_amount (Union[Unset, float]):
        as_of (Union[Unset, str]):
        confidence (Union[Unset, CloudConnectionBillingCurrentPeriodEstimateConfidence]):
        currency (Union[Unset, str]):
    """

    total_amount: Union[Unset, float] = UNSET
    forecast_amount: Union[Unset, float] = UNSET
    as_of: Union[Unset, str] = UNSET
    confidence: Union[Unset, CloudConnectionBillingCurrentPeriodEstimateConfidence] = (
        UNSET
    )
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_amount = self.total_amount

        forecast_amount = self.forecast_amount

        as_of = self.as_of

        confidence: Union[Unset, str] = UNSET
        if not isinstance(self.confidence, Unset):
            confidence = self.confidence

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if forecast_amount is not UNSET:
            field_dict["forecastAmount"] = forecast_amount
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_amount = d.pop("totalAmount", UNSET)

        forecast_amount = d.pop("forecastAmount", UNSET)

        as_of = d.pop("asOf", UNSET)

        _confidence = d.pop("confidence", UNSET)
        confidence: Union[Unset, CloudConnectionBillingCurrentPeriodEstimateConfidence]
        if isinstance(_confidence, Unset):
            confidence = UNSET
        else:
            confidence = (
                check_cloud_connection_billing_current_period_estimate_confidence(
                    _confidence
                )
            )

        currency = d.pop("currency", UNSET)

        cloud_connection_billing_current_period_estimate = cls(
            total_amount=total_amount,
            forecast_amount=forecast_amount,
            as_of=as_of,
            confidence=confidence,
            currency=currency,
        )

        cloud_connection_billing_current_period_estimate.additional_properties = d
        return cloud_connection_billing_current_period_estimate

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
