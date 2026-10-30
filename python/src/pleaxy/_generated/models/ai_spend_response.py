from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_spend_group import AiSpendGroup
    from ..models.ai_spend_response_not_readable_item import (
        AiSpendResponseNotReadableItem,
    )
    from ..models.ai_spend_total import AiSpendTotal
    from ..models.ai_spend_unattributed import AiSpendUnattributed


T = TypeVar("T", bound="AiSpendResponse")


@_attrs_define
class AiSpendResponse:
    """
    Attributes:
        period (Union[Unset, str]):
        as_of (Union[Unset, str]):
        totals (Union[Unset, List['AiSpendTotal']]):
        groups (Union[Unset, List['AiSpendGroup']]):
        unattributed (Union[Unset, List['AiSpendUnattributed']]):
        not_readable (Union[Unset, List['AiSpendResponseNotReadableItem']]):
    """

    period: Union[Unset, str] = UNSET
    as_of: Union[Unset, str] = UNSET
    totals: Union[Unset, List["AiSpendTotal"]] = UNSET
    groups: Union[Unset, List["AiSpendGroup"]] = UNSET
    unattributed: Union[Unset, List["AiSpendUnattributed"]] = UNSET
    not_readable: Union[Unset, List["AiSpendResponseNotReadableItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        period = self.period

        as_of = self.as_of

        totals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = []
            for totals_item_data in self.totals:
                totals_item = totals_item_data.to_dict()
                totals.append(totals_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        unattributed: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unattributed, Unset):
            unattributed = []
            for unattributed_item_data in self.unattributed:
                unattributed_item = unattributed_item_data.to_dict()
                unattributed.append(unattributed_item)

        not_readable: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.not_readable, Unset):
            not_readable = []
            for not_readable_item_data in self.not_readable:
                not_readable_item = not_readable_item_data.to_dict()
                not_readable.append(not_readable_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if as_of is not UNSET:
            field_dict["asOf"] = as_of
        if totals is not UNSET:
            field_dict["totals"] = totals
        if groups is not UNSET:
            field_dict["groups"] = groups
        if unattributed is not UNSET:
            field_dict["unattributed"] = unattributed
        if not_readable is not UNSET:
            field_dict["notReadable"] = not_readable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_spend_group import AiSpendGroup
        from ..models.ai_spend_response_not_readable_item import (
            AiSpendResponseNotReadableItem,
        )
        from ..models.ai_spend_total import AiSpendTotal
        from ..models.ai_spend_unattributed import AiSpendUnattributed

        d = src_dict.copy()
        period = d.pop("period", UNSET)

        as_of = d.pop("asOf", UNSET)

        totals = []
        _totals = d.pop("totals", UNSET)
        for totals_item_data in _totals or []:
            totals_item = AiSpendTotal.from_dict(totals_item_data)

            totals.append(totals_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = AiSpendGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        unattributed = []
        _unattributed = d.pop("unattributed", UNSET)
        for unattributed_item_data in _unattributed or []:
            unattributed_item = AiSpendUnattributed.from_dict(unattributed_item_data)

            unattributed.append(unattributed_item)

        not_readable = []
        _not_readable = d.pop("notReadable", UNSET)
        for not_readable_item_data in _not_readable or []:
            not_readable_item = AiSpendResponseNotReadableItem.from_dict(
                not_readable_item_data
            )

            not_readable.append(not_readable_item)

        ai_spend_response = cls(
            period=period,
            as_of=as_of,
            totals=totals,
            groups=groups,
            unattributed=unattributed,
            not_readable=not_readable,
        )

        ai_spend_response.additional_properties = d
        return ai_spend_response

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
