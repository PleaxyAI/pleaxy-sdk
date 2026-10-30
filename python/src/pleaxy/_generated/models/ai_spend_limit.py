from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_spend_limit_enforcement import (
    AiSpendLimitEnforcement,
    check_ai_spend_limit_enforcement,
)
from ..models.ai_spend_limit_invoicer import (
    AiSpendLimitInvoicer,
    check_ai_spend_limit_invoicer,
)
from ..models.ai_spend_limit_state import AiSpendLimitState, check_ai_spend_limit_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_spend_limit_history_item import AiSpendLimitHistoryItem
    from ..models.ai_spend_limit_read_back import AiSpendLimitReadBack


T = TypeVar("T", bound="AiSpendLimit")


@_attrs_define
class AiSpendLimit:
    """
    Attributes:
        po_id (Union[Unset, str]):
        line_no (Union[Unset, float]):
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiSpendLimitInvoicer]):
        target (Union[Unset, str]):
        amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        period (Union[Unset, str]):
        provider_ref (Union[Unset, str]):
        enforcement (Union[Unset, AiSpendLimitEnforcement]):
        state (Union[Unset, AiSpendLimitState]):
        read_back (Union[Unset, AiSpendLimitReadBack]):
        error (Union[Unset, str]):
        set_at (Union[Unset, str]):
        set_by (Union[Unset, str]):
        history (Union[Unset, List['AiSpendLimitHistoryItem']]):
    """

    po_id: Union[Unset, str] = UNSET
    line_no: Union[Unset, float] = UNSET
    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiSpendLimitInvoicer] = UNSET
    target: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    provider_ref: Union[Unset, str] = UNSET
    enforcement: Union[Unset, AiSpendLimitEnforcement] = UNSET
    state: Union[Unset, AiSpendLimitState] = UNSET
    read_back: Union[Unset, "AiSpendLimitReadBack"] = UNSET
    error: Union[Unset, str] = UNSET
    set_at: Union[Unset, str] = UNSET
    set_by: Union[Unset, str] = UNSET
    history: Union[Unset, List["AiSpendLimitHistoryItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        po_id = self.po_id

        line_no = self.line_no

        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        target = self.target

        amount = self.amount

        currency = self.currency

        period = self.period

        provider_ref = self.provider_ref

        enforcement: Union[Unset, str] = UNSET
        if not isinstance(self.enforcement, Unset):
            enforcement = self.enforcement

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        read_back: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.read_back, Unset):
            read_back = self.read_back.to_dict()

        error = self.error

        set_at = self.set_at

        set_by = self.set_by

        history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if target is not UNSET:
            field_dict["target"] = target
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if period is not UNSET:
            field_dict["period"] = period
        if provider_ref is not UNSET:
            field_dict["providerRef"] = provider_ref
        if enforcement is not UNSET:
            field_dict["enforcement"] = enforcement
        if state is not UNSET:
            field_dict["state"] = state
        if read_back is not UNSET:
            field_dict["readBack"] = read_back
        if error is not UNSET:
            field_dict["error"] = error
        if set_at is not UNSET:
            field_dict["setAt"] = set_at
        if set_by is not UNSET:
            field_dict["setBy"] = set_by
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_spend_limit_history_item import AiSpendLimitHistoryItem
        from ..models.ai_spend_limit_read_back import AiSpendLimitReadBack

        d = src_dict.copy()
        po_id = d.pop("poId", UNSET)

        line_no = d.pop("lineNo", UNSET)

        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiSpendLimitInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_spend_limit_invoicer(_invoicer)

        target = d.pop("target", UNSET)

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        period = d.pop("period", UNSET)

        provider_ref = d.pop("providerRef", UNSET)

        _enforcement = d.pop("enforcement", UNSET)
        enforcement: Union[Unset, AiSpendLimitEnforcement]
        if isinstance(_enforcement, Unset):
            enforcement = UNSET
        else:
            enforcement = check_ai_spend_limit_enforcement(_enforcement)

        _state = d.pop("state", UNSET)
        state: Union[Unset, AiSpendLimitState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_ai_spend_limit_state(_state)

        _read_back = d.pop("readBack", UNSET)
        read_back: Union[Unset, AiSpendLimitReadBack]
        if isinstance(_read_back, Unset):
            read_back = UNSET
        else:
            read_back = AiSpendLimitReadBack.from_dict(_read_back)

        error = d.pop("error", UNSET)

        set_at = d.pop("setAt", UNSET)

        set_by = d.pop("setBy", UNSET)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = AiSpendLimitHistoryItem.from_dict(history_item_data)

            history.append(history_item)

        ai_spend_limit = cls(
            po_id=po_id,
            line_no=line_no,
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            target=target,
            amount=amount,
            currency=currency,
            period=period,
            provider_ref=provider_ref,
            enforcement=enforcement,
            state=state,
            read_back=read_back,
            error=error,
            set_at=set_at,
            set_by=set_by,
            history=history,
        )

        ai_spend_limit.additional_properties = d
        return ai_spend_limit

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
