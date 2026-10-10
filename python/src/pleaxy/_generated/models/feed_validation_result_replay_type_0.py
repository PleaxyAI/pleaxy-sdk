from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedValidationResultReplayType0")


@_attrs_define
class FeedValidationResultReplayType0:
    """
    Attributes:
        invoice_id (Union[Unset, str]):
        identical (Union[Unset, bool]):
    """

    invoice_id: Union[Unset, str] = UNSET
    identical: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id

        identical = self.identical

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if identical is not UNSET:
            field_dict["identical"] = identical

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoiceId", UNSET)

        identical = d.pop("identical", UNSET)

        feed_validation_result_replay_type_0 = cls(
            invoice_id=invoice_id,
            identical=identical,
        )

        feed_validation_result_replay_type_0.additional_properties = d
        return feed_validation_result_replay_type_0

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
