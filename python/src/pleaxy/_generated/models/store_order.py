from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.store_order_status import StoreOrderStatus, check_store_order_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.store_order_refusal import StoreOrderRefusal
    from ..models.store_order_store_answer import StoreOrderStoreAnswer


T = TypeVar("T", bound="StoreOrder")


@_attrs_define
class StoreOrder:
    """
    Attributes:
        status (Union[Unset, StoreOrderStatus]):
        payload_id (Union[Unset, str]):
        attempts (Union[Unset, float]):
        queued_at (Union[Unset, str]):
        last_attempt_at (Union[Unset, str]):
        next_attempt_at (Union[Unset, str]):
        sent_at (Union[Unset, str]):
        refusal (Union[Unset, StoreOrderRefusal]):
        store_answer (Union[Unset, StoreOrderStoreAnswer]):
        deadline (Union[Unset, str]):
        queue_sk (Union[Unset, str]):
    """

    status: Union[Unset, StoreOrderStatus] = UNSET
    payload_id: Union[Unset, str] = UNSET
    attempts: Union[Unset, float] = UNSET
    queued_at: Union[Unset, str] = UNSET
    last_attempt_at: Union[Unset, str] = UNSET
    next_attempt_at: Union[Unset, str] = UNSET
    sent_at: Union[Unset, str] = UNSET
    refusal: Union[Unset, "StoreOrderRefusal"] = UNSET
    store_answer: Union[Unset, "StoreOrderStoreAnswer"] = UNSET
    deadline: Union[Unset, str] = UNSET
    queue_sk: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        payload_id = self.payload_id

        attempts = self.attempts

        queued_at = self.queued_at

        last_attempt_at = self.last_attempt_at

        next_attempt_at = self.next_attempt_at

        sent_at = self.sent_at

        refusal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refusal, Unset):
            refusal = self.refusal.to_dict()

        store_answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.store_answer, Unset):
            store_answer = self.store_answer.to_dict()

        deadline = self.deadline

        queue_sk = self.queue_sk

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if payload_id is not UNSET:
            field_dict["payloadId"] = payload_id
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at
        if last_attempt_at is not UNSET:
            field_dict["lastAttemptAt"] = last_attempt_at
        if next_attempt_at is not UNSET:
            field_dict["nextAttemptAt"] = next_attempt_at
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at
        if refusal is not UNSET:
            field_dict["refusal"] = refusal
        if store_answer is not UNSET:
            field_dict["storeAnswer"] = store_answer
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if queue_sk is not UNSET:
            field_dict["queueSk"] = queue_sk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.store_order_refusal import StoreOrderRefusal
        from ..models.store_order_store_answer import StoreOrderStoreAnswer

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, StoreOrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_store_order_status(_status)

        payload_id = d.pop("payloadId", UNSET)

        attempts = d.pop("attempts", UNSET)

        queued_at = d.pop("queuedAt", UNSET)

        last_attempt_at = d.pop("lastAttemptAt", UNSET)

        next_attempt_at = d.pop("nextAttemptAt", UNSET)

        sent_at = d.pop("sentAt", UNSET)

        _refusal = d.pop("refusal", UNSET)
        refusal: Union[Unset, StoreOrderRefusal]
        if isinstance(_refusal, Unset):
            refusal = UNSET
        else:
            refusal = StoreOrderRefusal.from_dict(_refusal)

        _store_answer = d.pop("storeAnswer", UNSET)
        store_answer: Union[Unset, StoreOrderStoreAnswer]
        if isinstance(_store_answer, Unset):
            store_answer = UNSET
        else:
            store_answer = StoreOrderStoreAnswer.from_dict(_store_answer)

        deadline = d.pop("deadline", UNSET)

        queue_sk = d.pop("queueSk", UNSET)

        store_order = cls(
            status=status,
            payload_id=payload_id,
            attempts=attempts,
            queued_at=queued_at,
            last_attempt_at=last_attempt_at,
            next_attempt_at=next_attempt_at,
            sent_at=sent_at,
            refusal=refusal,
            store_answer=store_answer,
            deadline=deadline,
            queue_sk=queue_sk,
        )

        store_order.additional_properties = d
        return store_order

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
