from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.buyer_sourcing_invitee_view_state import (
    BuyerSourcingInviteeViewState,
    check_buyer_sourcing_invitee_view_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyerSourcingInviteeView")


@_attrs_define
class BuyerSourcingInviteeView:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        supplier_connection_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        email (Union[Unset, str]):
        on_pleaxy (Union[Unset, bool]):
        state (Union[Unset, BuyerSourcingInviteeViewState]):
        decline_reason (Union[Unset, str]):
        invited_at (Union[Unset, str]):
        viewed_at (Union[Unset, str]):
        declined_at (Union[Unset, str]):
        submitted_at (Union[Unset, str]):
        submissions (Union[Unset, float]):
        shortlisted (Union[Unset, bool]):
    """

    supplier_key: Union[Unset, str] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    on_pleaxy: Union[Unset, bool] = UNSET
    state: Union[Unset, BuyerSourcingInviteeViewState] = UNSET
    decline_reason: Union[Unset, str] = UNSET
    invited_at: Union[Unset, str] = UNSET
    viewed_at: Union[Unset, str] = UNSET
    declined_at: Union[Unset, str] = UNSET
    submitted_at: Union[Unset, str] = UNSET
    submissions: Union[Unset, float] = UNSET
    shortlisted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        supplier_connection_id = self.supplier_connection_id

        supplier_name = self.supplier_name

        email = self.email

        on_pleaxy = self.on_pleaxy

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        decline_reason = self.decline_reason

        invited_at = self.invited_at

        viewed_at = self.viewed_at

        declined_at = self.declined_at

        submitted_at = self.submitted_at

        submissions = self.submissions

        shortlisted = self.shortlisted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if email is not UNSET:
            field_dict["email"] = email
        if on_pleaxy is not UNSET:
            field_dict["onPleaxy"] = on_pleaxy
        if state is not UNSET:
            field_dict["state"] = state
        if decline_reason is not UNSET:
            field_dict["declineReason"] = decline_reason
        if invited_at is not UNSET:
            field_dict["invitedAt"] = invited_at
        if viewed_at is not UNSET:
            field_dict["viewedAt"] = viewed_at
        if declined_at is not UNSET:
            field_dict["declinedAt"] = declined_at
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if submissions is not UNSET:
            field_dict["submissions"] = submissions
        if shortlisted is not UNSET:
            field_dict["shortlisted"] = shortlisted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        email = d.pop("email", UNSET)

        on_pleaxy = d.pop("onPleaxy", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BuyerSourcingInviteeViewState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_buyer_sourcing_invitee_view_state(_state)

        decline_reason = d.pop("declineReason", UNSET)

        invited_at = d.pop("invitedAt", UNSET)

        viewed_at = d.pop("viewedAt", UNSET)

        declined_at = d.pop("declinedAt", UNSET)

        submitted_at = d.pop("submittedAt", UNSET)

        submissions = d.pop("submissions", UNSET)

        shortlisted = d.pop("shortlisted", UNSET)

        buyer_sourcing_invitee_view = cls(
            supplier_key=supplier_key,
            supplier_connection_id=supplier_connection_id,
            supplier_name=supplier_name,
            email=email,
            on_pleaxy=on_pleaxy,
            state=state,
            decline_reason=decline_reason,
            invited_at=invited_at,
            viewed_at=viewed_at,
            declined_at=declined_at,
            submitted_at=submitted_at,
            submissions=submissions,
            shortlisted=shortlisted,
        )

        buyer_sourcing_invitee_view.additional_properties = d
        return buyer_sourcing_invitee_view

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
