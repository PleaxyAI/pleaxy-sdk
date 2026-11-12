from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_criterion_kind import (
    SourcingCriterionKind,
    check_sourcing_criterion_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourcingCriterion")


@_attrs_define
class SourcingCriterion:
    """
    Attributes:
        id (str):
        name (Union[Unset, str]):
        weight (Union[Unset, float]):
        kind (Union[Unset, SourcingCriterionKind]):
    """

    id: str
    name: Union[Unset, str] = UNSET
    weight: Union[Unset, float] = UNSET
    kind: Union[Unset, SourcingCriterionKind] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        weight = self.weight

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if weight is not UNSET:
            field_dict["weight"] = weight
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name", UNSET)

        weight = d.pop("weight", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, SourcingCriterionKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_sourcing_criterion_kind(_kind)

        sourcing_criterion = cls(
            id=id,
            name=name,
            weight=weight,
            kind=kind,
        )

        sourcing_criterion.additional_properties = d
        return sourcing_criterion

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
