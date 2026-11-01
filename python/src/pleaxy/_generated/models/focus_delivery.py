from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_delivery_reason import (
    FocusDeliveryReason,
    check_focus_delivery_reason,
)
from ..models.focus_delivery_trigger import (
    FocusDeliveryTrigger,
    check_focus_delivery_trigger,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FocusDelivery")


@_attrs_define
class FocusDelivery:
    """
    Attributes:
        at (Union[Unset, str]):
        ok (Union[Unset, bool]):
        periods (Union[Unset, List[str]]):
        row_count (Union[Unset, float]):
        reason (Union[Unset, FocusDeliveryReason]):
        trigger (Union[Unset, FocusDeliveryTrigger]):
    """

    at: Union[Unset, str] = UNSET
    ok: Union[Unset, bool] = UNSET
    periods: Union[Unset, List[str]] = UNSET
    row_count: Union[Unset, float] = UNSET
    reason: Union[Unset, FocusDeliveryReason] = UNSET
    trigger: Union[Unset, FocusDeliveryTrigger] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        ok = self.ok

        periods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        row_count = self.row_count

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if ok is not UNSET:
            field_dict["ok"] = ok
        if periods is not UNSET:
            field_dict["periods"] = periods
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if reason is not UNSET:
            field_dict["reason"] = reason
        if trigger is not UNSET:
            field_dict["trigger"] = trigger

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        at = d.pop("at", UNSET)

        ok = d.pop("ok", UNSET)

        periods = cast(List[str], d.pop("periods", UNSET))

        row_count = d.pop("rowCount", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, FocusDeliveryReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_focus_delivery_reason(_reason)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, FocusDeliveryTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = check_focus_delivery_trigger(_trigger)

        focus_delivery = cls(
            at=at,
            ok=ok,
            periods=periods,
            row_count=row_count,
            reason=reason,
            trigger=trigger,
        )

        focus_delivery.additional_properties = d
        return focus_delivery

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
