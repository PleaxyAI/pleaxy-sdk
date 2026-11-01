from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_source_view import FocusSourceView


T = TypeVar("T", bound="ListFocusSourcesResult")


@_attrs_define
class ListFocusSourcesResult:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        sources (Union[Unset, List['FocusSourceView']]):
    """

    enabled: Union[Unset, bool] = UNSET
    sources: Union[Unset, List["FocusSourceView"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled

        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_source_view import FocusSourceView

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = FocusSourceView.from_dict(sources_item_data)

            sources.append(sources_item)

        list_focus_sources_result = cls(
            enabled=enabled,
            sources=sources,
        )

        list_focus_sources_result.additional_properties = d
        return list_focus_sources_result

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
