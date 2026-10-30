from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AiRenewalRuleLastRunDraftsItem")


@_attrs_define
class AiRenewalRuleLastRunDraftsItem:
    """
    Attributes:
        po_id (Union[Unset, str]):
        draft_id (Union[Unset, str]):
    """

    po_id: Union[Unset, str] = UNSET
    draft_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        po_id = self.po_id

        draft_id = self.draft_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if draft_id is not UNSET:
            field_dict["draftId"] = draft_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        po_id = d.pop("poId", UNSET)

        draft_id = d.pop("draftId", UNSET)

        ai_renewal_rule_last_run_drafts_item = cls(
            po_id=po_id,
            draft_id=draft_id,
        )

        ai_renewal_rule_last_run_drafts_item.additional_properties = d
        return ai_renewal_rule_last_run_drafts_item

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
