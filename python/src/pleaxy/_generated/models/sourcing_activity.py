from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_activity_action import (
    SourcingActivityAction,
    check_sourcing_activity_action,
)
from ..models.sourcing_activity_actor import (
    SourcingActivityActor,
    check_sourcing_activity_actor,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_activity_detail import SourcingActivityDetail


T = TypeVar("T", bound="SourcingActivity")


@_attrs_define
class SourcingActivity:
    """
    Attributes:
        at (Union[Unset, str]):
        actor (Union[Unset, SourcingActivityActor]):
        actor_name (Union[Unset, str]):
        action (Union[Unset, SourcingActivityAction]):
        supplier_key (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        detail (Union[Unset, SourcingActivityDetail]):
    """

    at: Union[Unset, str] = UNSET
    actor: Union[Unset, SourcingActivityActor] = UNSET
    actor_name: Union[Unset, str] = UNSET
    action: Union[Unset, SourcingActivityAction] = UNSET
    supplier_key: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    detail: Union[Unset, "SourcingActivityDetail"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        actor: Union[Unset, str] = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor

        actor_name = self.actor_name

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        supplier_key = self.supplier_key

        supplier_name = self.supplier_name

        detail: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if actor is not UNSET:
            field_dict["actor"] = actor
        if actor_name is not UNSET:
            field_dict["actorName"] = actor_name
        if action is not UNSET:
            field_dict["action"] = action
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_activity_detail import SourcingActivityDetail

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _actor = d.pop("actor", UNSET)
        actor: Union[Unset, SourcingActivityActor]
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = check_sourcing_activity_actor(_actor)

        actor_name = d.pop("actorName", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, SourcingActivityAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_sourcing_activity_action(_action)

        supplier_key = d.pop("supplierKey", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        _detail = d.pop("detail", UNSET)
        detail: Union[Unset, SourcingActivityDetail]
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = SourcingActivityDetail.from_dict(_detail)

        sourcing_activity = cls(
            at=at,
            actor=actor,
            actor_name=actor_name,
            action=action,
            supplier_key=supplier_key,
            supplier_name=supplier_name,
            detail=detail,
        )

        sourcing_activity.additional_properties = d
        return sourcing_activity

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
