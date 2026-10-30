from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_spend_response_not_readable_item_invoicer import (
    AiSpendResponseNotReadableItemInvoicer,
    check_ai_spend_response_not_readable_item_invoicer,
)
from ..models.ai_spend_response_not_readable_item_reason import (
    AiSpendResponseNotReadableItemReason,
    check_ai_spend_response_not_readable_item_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AiSpendResponseNotReadableItem")


@_attrs_define
class AiSpendResponseNotReadableItem:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiSpendResponseNotReadableItemInvoicer]):
        label (Union[Unset, str]):
        reason (Union[Unset, AiSpendResponseNotReadableItemReason]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiSpendResponseNotReadableItemInvoicer] = UNSET
    label: Union[Unset, str] = UNSET
    reason: Union[Unset, AiSpendResponseNotReadableItemReason] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        label = self.label

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if label is not UNSET:
            field_dict["label"] = label
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiSpendResponseNotReadableItemInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_spend_response_not_readable_item_invoicer(_invoicer)

        label = d.pop("label", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, AiSpendResponseNotReadableItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_ai_spend_response_not_readable_item_reason(_reason)

        ai_spend_response_not_readable_item = cls(
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            label=label,
            reason=reason,
        )

        ai_spend_response_not_readable_item.additional_properties = d
        return ai_spend_response_not_readable_item

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
