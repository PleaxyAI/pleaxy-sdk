from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cloud_bulk_account_view_source import (
    CloudBulkAccountViewSource,
    check_cloud_bulk_account_view_source,
)
from ..models.cloud_bulk_account_view_state import (
    CloudBulkAccountViewState,
    check_cloud_bulk_account_view_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudBulkAccountView")


@_attrs_define
class CloudBulkAccountView:
    """
    Attributes:
        account_id (Union[Unset, str]):
        source (Union[Unset, CloudBulkAccountViewSource]):
        state (Union[Unset, CloudBulkAccountViewState]):
        attempts (Union[Unset, float]):
        next_attempt_at (Union[Unset, str]):
        failed_at (Union[Unset, str]):
        cost_center (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    source: Union[Unset, CloudBulkAccountViewSource] = UNSET
    state: Union[Unset, CloudBulkAccountViewState] = UNSET
    attempts: Union[Unset, float] = UNSET
    next_attempt_at: Union[Unset, str] = UNSET
    failed_at: Union[Unset, str] = UNSET
    cost_center: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        attempts = self.attempts

        next_attempt_at = self.next_attempt_at

        failed_at = self.failed_at

        cost_center = self.cost_center

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if next_attempt_at is not UNSET:
            field_dict["nextAttemptAt"] = next_attempt_at
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, CloudBulkAccountViewSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_cloud_bulk_account_view_source(_source)

        _state = d.pop("state", UNSET)
        state: Union[Unset, CloudBulkAccountViewState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_cloud_bulk_account_view_state(_state)

        attempts = d.pop("attempts", UNSET)

        next_attempt_at = d.pop("nextAttemptAt", UNSET)

        failed_at = d.pop("failedAt", UNSET)

        cost_center = d.pop("costCenter", UNSET)

        cloud_bulk_account_view = cls(
            account_id=account_id,
            source=source,
            state=state,
            attempts=attempts,
            next_attempt_at=next_attempt_at,
            failed_at=failed_at,
            cost_center=cost_center,
        )

        cloud_bulk_account_view.additional_properties = d
        return cloud_bulk_account_view

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
