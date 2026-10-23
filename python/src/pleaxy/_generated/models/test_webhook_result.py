from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_webhook_result_error_code import (
    TestWebhookResultErrorCode,
    check_test_webhook_result_error_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestWebhookResult")


@_attrs_define
class TestWebhookResult:
    """
    Attributes:
        ok (Union[Unset, bool]):
        status (Union[Unset, float]):
        error_code (Union[Unset, TestWebhookResultErrorCode]):
        duration_ms (Union[Unset, float]):
    """

    ok: Union[Unset, bool] = UNSET
    status: Union[Unset, float] = UNSET
    error_code: Union[Unset, TestWebhookResultErrorCode] = UNSET
    duration_ms: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ok = self.ok

        status = self.status

        error_code: Union[Unset, str] = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code

        duration_ms = self.duration_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ok is not UNSET:
            field_dict["ok"] = ok
        if status is not UNSET:
            field_dict["status"] = status
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ok = d.pop("ok", UNSET)

        status = d.pop("status", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: Union[Unset, TestWebhookResultErrorCode]
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_test_webhook_result_error_code(_error_code)

        duration_ms = d.pop("durationMs", UNSET)

        test_webhook_result = cls(
            ok=ok,
            status=status,
            error_code=error_code,
            duration_ms=duration_ms,
        )

        test_webhook_result.additional_properties = d
        return test_webhook_result

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
