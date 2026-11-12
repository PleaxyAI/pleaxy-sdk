from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comment_view import DocumentCommentView


T = TypeVar("T", bound="ListPurchaseOrderCommentsResult")


@_attrs_define
class ListPurchaseOrderCommentsResult:
    """
    Attributes:
        sharing (Union[Unset, str]):
        comments (Union[Unset, List['DocumentCommentView']]):
        awaiting_reply (Union[Unset, bool]):
        meeting_requests (Union[Unset, str]):
    """

    sharing: Union[Unset, str] = UNSET
    comments: Union[Unset, List["DocumentCommentView"]] = UNSET
    awaiting_reply: Union[Unset, bool] = UNSET
    meeting_requests: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sharing = self.sharing

        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        awaiting_reply = self.awaiting_reply

        meeting_requests = self.meeting_requests

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if comments is not UNSET:
            field_dict["comments"] = comments
        if awaiting_reply is not UNSET:
            field_dict["awaitingReply"] = awaiting_reply
        if meeting_requests is not UNSET:
            field_dict["meetingRequests"] = meeting_requests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_comment_view import DocumentCommentView

        d = src_dict.copy()
        sharing = d.pop("sharing", UNSET)

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = DocumentCommentView.from_dict(comments_item_data)

            comments.append(comments_item)

        awaiting_reply = d.pop("awaitingReply", UNSET)

        meeting_requests = d.pop("meetingRequests", UNSET)

        list_purchase_order_comments_result = cls(
            sharing=sharing,
            comments=comments,
            awaiting_reply=awaiting_reply,
            meeting_requests=meeting_requests,
        )

        list_purchase_order_comments_result.additional_properties = d
        return list_purchase_order_comments_result

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
