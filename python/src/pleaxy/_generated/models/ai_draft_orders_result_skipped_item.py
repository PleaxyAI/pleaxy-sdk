from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_draft_orders_result_skipped_item_reason import (
    AiDraftOrdersResultSkippedItemReason,
    check_ai_draft_orders_result_skipped_item_reason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_draft_orders_result_skipped_item_params import (
        AiDraftOrdersResultSkippedItemParams,
    )


T = TypeVar("T", bound="AiDraftOrdersResultSkippedItem")


@_attrs_define
class AiDraftOrdersResultSkippedItem:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        reason (Union[Unset, AiDraftOrdersResultSkippedItemReason]):
        po_id (Union[Unset, str]):
        message (Union[Unset, str]):
        message_id (Union[Unset, str]):
        params (Union[Unset, AiDraftOrdersResultSkippedItemParams]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    reason: Union[Unset, AiDraftOrdersResultSkippedItemReason] = UNSET
    po_id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    params: Union[Unset, "AiDraftOrdersResultSkippedItemParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        po_id = self.po_id

        message = self.message

        message_id = self.message_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if message is not UNSET:
            field_dict["message"] = message
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_draft_orders_result_skipped_item_params import (
            AiDraftOrdersResultSkippedItemParams,
        )

        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, AiDraftOrdersResultSkippedItemReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_ai_draft_orders_result_skipped_item_reason(_reason)

        po_id = d.pop("poId", UNSET)

        message = d.pop("message", UNSET)

        message_id = d.pop("messageId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, AiDraftOrdersResultSkippedItemParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = AiDraftOrdersResultSkippedItemParams.from_dict(_params)

        ai_draft_orders_result_skipped_item = cls(
            invoicer_id=invoicer_id,
            reason=reason,
            po_id=po_id,
            message=message,
            message_id=message_id,
            params=params,
        )

        ai_draft_orders_result_skipped_item.additional_properties = d
        return ai_draft_orders_result_skipped_item

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
