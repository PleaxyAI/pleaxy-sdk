from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_stripe_payment_result_state import (
    StartStripePaymentResultState,
    check_start_stripe_payment_result_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartStripePaymentResult")


@_attrs_define
class StartStripePaymentResult:
    """
    Attributes:
        url (Union[Unset, str]):
        state (Union[Unset, StartStripePaymentResultState]):
    """

    url: Union[Unset, str] = UNSET
    state: Union[Unset, StartStripePaymentResultState] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, StartStripePaymentResultState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_start_stripe_payment_result_state(_state)

        start_stripe_payment_result = cls(
            url=url,
            state=state,
        )

        start_stripe_payment_result.additional_properties = d
        return start_stripe_payment_result

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
