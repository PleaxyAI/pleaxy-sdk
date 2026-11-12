from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_comment_view_author_side import (
    DocumentCommentViewAuthorSide,
    check_document_comment_view_author_side,
)
from ..models.document_comment_view_document_kind import (
    DocumentCommentViewDocumentKind,
    check_document_comment_view_document_kind,
)
from ..models.document_comment_view_visibility import (
    DocumentCommentViewVisibility,
    check_document_comment_view_visibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_meeting_view import CommentMeetingView
    from ..models.comment_mention import CommentMention


T = TypeVar("T", bound="DocumentCommentView")


@_attrs_define
class DocumentCommentView:
    """
    Attributes:
        id (str):
        author_key (Union[Unset, str]):
        mentions (Union[Unset, List['CommentMention']]):
        meeting (Union[Unset, CommentMeetingView]):
        viewer_is_author (Union[Unset, bool]):
        created_at (Union[Unset, str]):
        document_kind (Union[Unset, DocumentCommentViewDocumentKind]):
        document_id (Union[Unset, str]):
        body (Union[Unset, str]):
        visibility (Union[Unset, DocumentCommentViewVisibility]):
        author_side (Union[Unset, DocumentCommentViewAuthorSide]):
        author_name (Union[Unset, str]):
        author_org_name (Union[Unset, str]):
        deleted_at (Union[Unset, str]):
    """

    id: str
    author_key: Union[Unset, str] = UNSET
    mentions: Union[Unset, List["CommentMention"]] = UNSET
    meeting: Union[Unset, "CommentMeetingView"] = UNSET
    viewer_is_author: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    document_kind: Union[Unset, DocumentCommentViewDocumentKind] = UNSET
    document_id: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    visibility: Union[Unset, DocumentCommentViewVisibility] = UNSET
    author_side: Union[Unset, DocumentCommentViewAuthorSide] = UNSET
    author_name: Union[Unset, str] = UNSET
    author_org_name: Union[Unset, str] = UNSET
    deleted_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        author_key = self.author_key

        mentions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = []
            for mentions_item_data in self.mentions:
                mentions_item = mentions_item_data.to_dict()
                mentions.append(mentions_item)

        meeting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meeting, Unset):
            meeting = self.meeting.to_dict()

        viewer_is_author = self.viewer_is_author

        created_at = self.created_at

        document_kind: Union[Unset, str] = UNSET
        if not isinstance(self.document_kind, Unset):
            document_kind = self.document_kind

        document_id = self.document_id

        body = self.body

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        author_side: Union[Unset, str] = UNSET
        if not isinstance(self.author_side, Unset):
            author_side = self.author_side

        author_name = self.author_name

        author_org_name = self.author_org_name

        deleted_at = self.deleted_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if author_key is not UNSET:
            field_dict["authorKey"] = author_key
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if meeting is not UNSET:
            field_dict["meeting"] = meeting
        if viewer_is_author is not UNSET:
            field_dict["viewerIsAuthor"] = viewer_is_author
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if document_kind is not UNSET:
            field_dict["documentKind"] = document_kind
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if body is not UNSET:
            field_dict["body"] = body
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if author_side is not UNSET:
            field_dict["authorSide"] = author_side
        if author_name is not UNSET:
            field_dict["authorName"] = author_name
        if author_org_name is not UNSET:
            field_dict["authorOrgName"] = author_org_name
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_meeting_view import CommentMeetingView
        from ..models.comment_mention import CommentMention

        d = src_dict.copy()
        id = d.pop("id")

        author_key = d.pop("authorKey", UNSET)

        mentions = []
        _mentions = d.pop("mentions", UNSET)
        for mentions_item_data in _mentions or []:
            mentions_item = CommentMention.from_dict(mentions_item_data)

            mentions.append(mentions_item)

        _meeting = d.pop("meeting", UNSET)
        meeting: Union[Unset, CommentMeetingView]
        if isinstance(_meeting, Unset):
            meeting = UNSET
        else:
            meeting = CommentMeetingView.from_dict(_meeting)

        viewer_is_author = d.pop("viewerIsAuthor", UNSET)

        created_at = d.pop("createdAt", UNSET)

        _document_kind = d.pop("documentKind", UNSET)
        document_kind: Union[Unset, DocumentCommentViewDocumentKind]
        if isinstance(_document_kind, Unset):
            document_kind = UNSET
        else:
            document_kind = check_document_comment_view_document_kind(_document_kind)

        document_id = d.pop("documentId", UNSET)

        body = d.pop("body", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, DocumentCommentViewVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_document_comment_view_visibility(_visibility)

        _author_side = d.pop("authorSide", UNSET)
        author_side: Union[Unset, DocumentCommentViewAuthorSide]
        if isinstance(_author_side, Unset):
            author_side = UNSET
        else:
            author_side = check_document_comment_view_author_side(_author_side)

        author_name = d.pop("authorName", UNSET)

        author_org_name = d.pop("authorOrgName", UNSET)

        deleted_at = d.pop("deletedAt", UNSET)

        document_comment_view = cls(
            id=id,
            author_key=author_key,
            mentions=mentions,
            meeting=meeting,
            viewer_is_author=viewer_is_author,
            created_at=created_at,
            document_kind=document_kind,
            document_id=document_id,
            body=body,
            visibility=visibility,
            author_side=author_side,
            author_name=author_name,
            author_org_name=author_org_name,
            deleted_at=deleted_at,
        )

        document_comment_view.additional_properties = d
        return document_comment_view

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
