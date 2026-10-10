from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_attempt import FeedAttempt


T = TypeVar("T", bound="FeedAttemptsPage")


@_attrs_define
class FeedAttemptsPage:
    """
    Attributes:
        attempts (Union[Unset, List['FeedAttempt']]):
        before (Union[Unset, str]):
    """

    attempts: Union[Unset, List["FeedAttempt"]] = UNSET
    before: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attempts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()
                attempts.append(attempts_item)

        before = self.before

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feed_attempt import FeedAttempt

        d = src_dict.copy()
        attempts = []
        _attempts = d.pop("attempts", UNSET)
        for attempts_item_data in _attempts or []:
            attempts_item = FeedAttempt.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        before = d.pop("before", UNSET)

        feed_attempts_page = cls(
            attempts=attempts,
            before=before,
        )

        feed_attempts_page.additional_properties = d
        return feed_attempts_page

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
