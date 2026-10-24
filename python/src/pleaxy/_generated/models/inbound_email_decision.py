from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inbound_email_decision_action import (
    InboundEmailDecisionAction,
    check_inbound_email_decision_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundEmailDecision")


@_attrs_define
class InboundEmailDecision:
    """
    Attributes:
        action (Union[Unset, InboundEmailDecisionAction]):
        by (Union[Unset, str]):
        at (Union[Unset, str]):
        confirmation_id (Union[Unset, str]):
        shipment_id (Union[Unset, str]):
    """

    action: Union[Unset, InboundEmailDecisionAction] = UNSET
    by: Union[Unset, str] = UNSET
    at: Union[Unset, str] = UNSET
    confirmation_id: Union[Unset, str] = UNSET
    shipment_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        by = self.by

        at = self.at

        confirmation_id = self.confirmation_id

        shipment_id = self.shipment_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if by is not UNSET:
            field_dict["by"] = by
        if at is not UNSET:
            field_dict["at"] = at
        if confirmation_id is not UNSET:
            field_dict["confirmationId"] = confirmation_id
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, InboundEmailDecisionAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_inbound_email_decision_action(_action)

        by = d.pop("by", UNSET)

        at = d.pop("at", UNSET)

        confirmation_id = d.pop("confirmationId", UNSET)

        shipment_id = d.pop("shipmentId", UNSET)

        inbound_email_decision = cls(
            action=action,
            by=by,
            at=at,
            confirmation_id=confirmation_id,
            shipment_id=shipment_id,
        )

        inbound_email_decision.additional_properties = d
        return inbound_email_decision

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
