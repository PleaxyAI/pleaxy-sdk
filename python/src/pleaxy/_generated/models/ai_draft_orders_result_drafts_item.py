from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiDraftOrdersResultDraftsItem")


@_attrs_define
class AiDraftOrdersResultDraftsItem:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        po_id (Union[Unset, str]):
        currency (Union[Unset, str]):
        total (Union[Unset, float]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    po_id: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        po_id = self.po_id

        currency = self.currency

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        po_id = d.pop("poId", UNSET)

        currency = d.pop("currency", UNSET)

        total = d.pop("total", UNSET)

        ai_draft_orders_result_drafts_item = cls(
            invoicer_id=invoicer_id,
            po_id=po_id,
            currency=currency,
            total=total,
        )

        ai_draft_orders_result_drafts_item.additional_properties = d
        return ai_draft_orders_result_drafts_item

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
