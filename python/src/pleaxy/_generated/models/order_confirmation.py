from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_confirmation_operation import (
    OrderConfirmationOperation,
    check_order_confirmation_operation,
)
from ..models.order_confirmation_outcome import (
    OrderConfirmationOutcome,
    check_order_confirmation_outcome,
)
from ..models.order_confirmation_source import (
    OrderConfirmationSource,
    check_order_confirmation_source,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_confirmation_decision import OrderConfirmationDecision
    from ..models.order_confirmation_line import OrderConfirmationLine


T = TypeVar("T", bound="OrderConfirmation")


@_attrs_define
class OrderConfirmation:
    """
    Attributes:
        id (str):
        po_id (Union[Unset, str]):
        outcome (Union[Unset, OrderConfirmationOutcome]):
        confirm_id (Union[Unset, str]):
        operation (Union[Unset, OrderConfirmationOperation]):
        delivery_date (Union[Unset, str]):
        note (Union[Unset, str]):
        lines (Union[Unset, List['OrderConfirmationLine']]):
        source (Union[Unset, OrderConfirmationSource]):
        created_at (Union[Unset, str]):
        decision (Union[Unset, OrderConfirmationDecision]):
    """

    id: str
    po_id: Union[Unset, str] = UNSET
    outcome: Union[Unset, OrderConfirmationOutcome] = UNSET
    confirm_id: Union[Unset, str] = UNSET
    operation: Union[Unset, OrderConfirmationOperation] = UNSET
    delivery_date: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    lines: Union[Unset, List["OrderConfirmationLine"]] = UNSET
    source: Union[Unset, OrderConfirmationSource] = UNSET
    created_at: Union[Unset, str] = UNSET
    decision: Union[Unset, "OrderConfirmationDecision"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        po_id = self.po_id

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        confirm_id = self.confirm_id

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation

        delivery_date = self.delivery_date

        note = self.note

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        created_at = self.created_at

        decision: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if confirm_id is not UNSET:
            field_dict["confirmId"] = confirm_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if delivery_date is not UNSET:
            field_dict["deliveryDate"] = delivery_date
        if note is not UNSET:
            field_dict["note"] = note
        if lines is not UNSET:
            field_dict["lines"] = lines
        if source is not UNSET:
            field_dict["source"] = source
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_confirmation_decision import OrderConfirmationDecision
        from ..models.order_confirmation_line import OrderConfirmationLine

        d = src_dict.copy()
        id = d.pop("id")

        po_id = d.pop("poId", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, OrderConfirmationOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_order_confirmation_outcome(_outcome)

        confirm_id = d.pop("confirmId", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, OrderConfirmationOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = check_order_confirmation_operation(_operation)

        delivery_date = d.pop("deliveryDate", UNSET)

        note = d.pop("note", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = OrderConfirmationLine.from_dict(lines_item_data)

            lines.append(lines_item)

        _source = d.pop("source", UNSET)
        source: Union[Unset, OrderConfirmationSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_order_confirmation_source(_source)

        created_at = d.pop("createdAt", UNSET)

        _decision = d.pop("decision", UNSET)
        decision: Union[Unset, OrderConfirmationDecision]
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = OrderConfirmationDecision.from_dict(_decision)

        order_confirmation = cls(
            id=id,
            po_id=po_id,
            outcome=outcome,
            confirm_id=confirm_id,
            operation=operation,
            delivery_date=delivery_date,
            note=note,
            lines=lines,
            source=source,
            created_at=created_at,
            decision=decision,
        )

        order_confirmation.additional_properties = d
        return order_confirmation

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
