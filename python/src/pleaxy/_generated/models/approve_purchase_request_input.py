from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovePurchaseRequestInput")


@_attrs_define
class ApprovePurchaseRequestInput:
    """
    Attributes:
        expected_version (Union[Unset, float]): The approval version the caller saw; refused with 409 if the request
            moved since.
    """

    expected_version: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expected_version = self.expected_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_version is not UNSET:
            field_dict["expectedVersion"] = expected_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expected_version = d.pop("expectedVersion", UNSET)

        approve_purchase_request_input = cls(
            expected_version=expected_version,
        )

        approve_purchase_request_input.additional_properties = d
        return approve_purchase_request_input

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
