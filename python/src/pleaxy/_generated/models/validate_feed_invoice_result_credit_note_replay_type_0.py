from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateFeedInvoiceResultCreditNoteReplayType0")


@_attrs_define
class ValidateFeedInvoiceResultCreditNoteReplayType0:
    """
    Attributes:
        credit_note_id (Union[Unset, str]):
        identical (Union[Unset, bool]):
    """

    credit_note_id: Union[Unset, str] = UNSET
    identical: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credit_note_id = self.credit_note_id

        identical = self.identical

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credit_note_id is not UNSET:
            field_dict["creditNoteId"] = credit_note_id
        if identical is not UNSET:
            field_dict["identical"] = identical

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credit_note_id = d.pop("creditNoteId", UNSET)

        identical = d.pop("identical", UNSET)

        validate_feed_invoice_result_credit_note_replay_type_0 = cls(
            credit_note_id=credit_note_id,
            identical=identical,
        )

        validate_feed_invoice_result_credit_note_replay_type_0.additional_properties = d
        return validate_feed_invoice_result_credit_note_replay_type_0

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
