from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_draft_orders_result_drafts_item import (
        AiDraftOrdersResultDraftsItem,
    )
    from ..models.ai_draft_orders_result_skipped_item import (
        AiDraftOrdersResultSkippedItem,
    )


T = TypeVar("T", bound="AiDraftOrdersResult")


@_attrs_define
class AiDraftOrdersResult:
    """
    Attributes:
        period (Union[Unset, str]):
        drafts (Union[Unset, List['AiDraftOrdersResultDraftsItem']]):
        skipped (Union[Unset, List['AiDraftOrdersResultSkippedItem']]):
    """

    period: Union[Unset, str] = UNSET
    drafts: Union[Unset, List["AiDraftOrdersResultDraftsItem"]] = UNSET
    skipped: Union[Unset, List["AiDraftOrdersResultSkippedItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        drafts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.drafts, Unset):
            drafts = []
            for drafts_item_data in self.drafts:
                drafts_item = drafts_item_data.to_dict()
                drafts.append(drafts_item)

        skipped: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if drafts is not UNSET:
            field_dict["drafts"] = drafts
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_draft_orders_result_drafts_item import (
            AiDraftOrdersResultDraftsItem,
        )
        from ..models.ai_draft_orders_result_skipped_item import (
            AiDraftOrdersResultSkippedItem,
        )

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        drafts = []
        _drafts = d.pop("drafts", UNSET)
        for drafts_item_data in _drafts or []:
            drafts_item = AiDraftOrdersResultDraftsItem.from_dict(drafts_item_data)

            drafts.append(drafts_item)

        skipped = []
        _skipped = d.pop("skipped", UNSET)
        for skipped_item_data in _skipped or []:
            skipped_item = AiDraftOrdersResultSkippedItem.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        ai_draft_orders_result = cls(
            period=period,
            drafts=drafts,
            skipped=skipped,
        )

        ai_draft_orders_result.additional_properties = d
        return ai_draft_orders_result

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
