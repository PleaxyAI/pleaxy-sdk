from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.screening_match_entry_kind import (
    ScreeningMatchEntryKind,
    check_screening_match_entry_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.screening_match_entry_identifiers_item import (
        ScreeningMatchEntryIdentifiersItem,
    )


T = TypeVar("T", bound="ScreeningMatchEntry")


@_attrs_define
class ScreeningMatchEntry:
    """
    Attributes:
        kind (Union[Unset, ScreeningMatchEntryKind]):
        names (Union[Unset, List[str]]):
        countries (Union[Unset, List[str]]):
        programmes (Union[Unset, List[str]]):
        identifiers (Union[Unset, List['ScreeningMatchEntryIdentifiersItem']]):
        listed_on (Union[Unset, str]):
    """

    kind: Union[Unset, ScreeningMatchEntryKind] = UNSET
    names: Union[Unset, List[str]] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    programmes: Union[Unset, List[str]] = UNSET
    identifiers: Union[Unset, List["ScreeningMatchEntryIdentifiersItem"]] = UNSET
    listed_on: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        programmes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.programmes, Unset):
            programmes = self.programmes

        identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        listed_on = self.listed_on

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if names is not UNSET:
            field_dict["names"] = names
        if countries is not UNSET:
            field_dict["countries"] = countries
        if programmes is not UNSET:
            field_dict["programmes"] = programmes
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if listed_on is not UNSET:
            field_dict["listedOn"] = listed_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.screening_match_entry_identifiers_item import (
            ScreeningMatchEntryIdentifiersItem,
        )

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, ScreeningMatchEntryKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_screening_match_entry_kind(_kind)

        names = cast(List[str], d.pop("names", UNSET))

        countries = cast(List[str], d.pop("countries", UNSET))

        programmes = cast(List[str], d.pop("programmes", UNSET))

        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for identifiers_item_data in _identifiers or []:
            identifiers_item = ScreeningMatchEntryIdentifiersItem.from_dict(
                identifiers_item_data
            )

            identifiers.append(identifiers_item)

        listed_on = d.pop("listedOn", UNSET)

        screening_match_entry = cls(
            kind=kind,
            names=names,
            countries=countries,
            programmes=programmes,
            identifiers=identifiers,
            listed_on=listed_on,
        )

        screening_match_entry.additional_properties = d
        return screening_match_entry

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
