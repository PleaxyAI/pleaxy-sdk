from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_usage_line import AiUsageLine


T = TypeVar("T", bound="AiUsageLinesPage")


@_attrs_define
class AiUsageLinesPage:
    """
    Attributes:
        lines (Union[Unset, List['AiUsageLine']]):
        next_cursor (Union[Unset, str]):
    """

    lines: Union[Unset, List["AiUsageLine"]] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        next_cursor = self.next_cursor

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines is not UNSET:
            field_dict["lines"] = lines
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_usage_line import AiUsageLine

        d = src_dict.copy()
        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = AiUsageLine.from_dict(lines_item_data)

            lines.append(lines_item)

        next_cursor = d.pop("nextCursor", UNSET)

        ai_usage_lines_page = cls(
            lines=lines,
            next_cursor=next_cursor,
        )

        ai_usage_lines_page.additional_properties = d
        return ai_usage_lines_page

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
