from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_item_input_line_type import (
    LineItemInputLineType,
    check_line_item_input_line_type,
)
from ..models.line_item_input_rule_type import (
    LineItemInputRuleType,
    check_line_item_input_rule_type,
)
from ..models.line_item_input_scope_type import (
    LineItemInputScopeType,
    check_line_item_input_scope_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_line_scope_input import AiLineScopeInput
    from ..models.punchout_ref_input import PunchoutRefInput


T = TypeVar("T", bound="LineItemInput")


@_attrs_define
class LineItemInput:
    """
    Attributes:
        scope_type (LineItemInputScopeType):
        name (str):
        rule_type (LineItemInputRuleType):
        unit (str):
        unit_price (float):
        qty (float):
        nte_amount (float):
        valid_from (str):
        valid_until (str):
        scope_id (Union[None, Unset, str]):
        line_type (Union[Unset, LineItemInputLineType]): goods (delivered: shipped and confirmed on a goods receipt) or
            service (performed: confirmed on a service entry sheet, never shipped). Defaults to the catalog item's type,
            else to service for a service scope or a time unit and goods otherwise.
        currency (Union[Unset, str]): ISO 4217. Optional - the server writes the order's currency on every line. If
            sent, it must be the order's currency (any case); another currency is a 400, since Pleaxy doesn't convert
            currencies.
        payment_terms (Union[Unset, str]): The line's payment terms, e.g. "Net 30". Optional: left out (or blank), the
            line takes the default payment terms of the contract it was priced from or the order names (contractId), else
            the catalog item's, else "Net 30".
        due_date (Union[Unset, str]): When the goods or the work on this line are due (YYYY-MM-DD), e.g. a statement-of-
            work milestone. On a 3-way order, its receiver is reminded when it passes with nothing received.
        customer_line_no (Union[Unset, str]): The buyer's own number for this line (e.g. from their ERP), up to 40
            characters. Optional, like poNumber; stored and shown alongside the server's lineNo, never replacing it.
        quote_line_no (Union[Unset, float]): The line of the order's quote (quoteImportId) this line was filled from,
            when Pleaxy read the quote. Kept on the line; the app shows the line as priced from the supplier's quote unless
            a contract rate priced it.
        sow_line_no (Union[Unset, float]): The milestone or deliverable of the order's statement of work (sowImportId)
            this line was filled from, when Pleaxy read the SOW. Kept on the line, provenance only, like quoteLineNo.
        punchout_ref (Union[Unset, PunchoutRefInput]):
        ai (Union[Unset, AiLineScopeInput]):
    """

    scope_type: LineItemInputScopeType
    name: str
    rule_type: LineItemInputRuleType
    unit: str
    unit_price: float
    qty: float
    nte_amount: float
    valid_from: str
    valid_until: str
    scope_id: Union[None, Unset, str] = UNSET
    line_type: Union[Unset, LineItemInputLineType] = UNSET
    currency: Union[Unset, str] = UNSET
    payment_terms: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    customer_line_no: Union[Unset, str] = UNSET
    quote_line_no: Union[Unset, float] = UNSET
    sow_line_no: Union[Unset, float] = UNSET
    punchout_ref: Union[Unset, "PunchoutRefInput"] = UNSET
    ai: Union[Unset, "AiLineScopeInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope_type: str = self.scope_type

        name = self.name

        rule_type: str = self.rule_type

        unit = self.unit

        unit_price = self.unit_price

        qty = self.qty

        nte_amount = self.nte_amount

        valid_from = self.valid_from

        valid_until = self.valid_until

        scope_id: Union[None, Unset, str]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        line_type: Union[Unset, str] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type

        currency = self.currency

        payment_terms = self.payment_terms

        due_date = self.due_date

        customer_line_no = self.customer_line_no

        quote_line_no = self.quote_line_no

        sow_line_no = self.sow_line_no

        punchout_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.punchout_ref, Unset):
            punchout_ref = self.punchout_ref.to_dict()

        ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scopeType": scope_type,
                "name": name,
                "ruleType": rule_type,
                "unit": unit,
                "unitPrice": unit_price,
                "qty": qty,
                "nteAmount": nte_amount,
                "validFrom": valid_from,
                "validUntil": valid_until,
            }
        )
        if scope_id is not UNSET:
            field_dict["scopeId"] = scope_id
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if customer_line_no is not UNSET:
            field_dict["customerLineNo"] = customer_line_no
        if quote_line_no is not UNSET:
            field_dict["quoteLineNo"] = quote_line_no
        if sow_line_no is not UNSET:
            field_dict["sowLineNo"] = sow_line_no
        if punchout_ref is not UNSET:
            field_dict["punchoutRef"] = punchout_ref
        if ai is not UNSET:
            field_dict["ai"] = ai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_line_scope_input import AiLineScopeInput
        from ..models.punchout_ref_input import PunchoutRefInput

        d = src_dict.copy()
        scope_type = check_line_item_input_scope_type(d.pop("scopeType"))

        name = d.pop("name")

        rule_type = check_line_item_input_rule_type(d.pop("ruleType"))

        unit = d.pop("unit")

        unit_price = d.pop("unitPrice")

        qty = d.pop("qty")

        nte_amount = d.pop("nteAmount")

        valid_from = d.pop("validFrom")

        valid_until = d.pop("validUntil")

        def _parse_scope_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_id = _parse_scope_id(d.pop("scopeId", UNSET))

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, LineItemInputLineType]
        if isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = check_line_item_input_line_type(_line_type)

        currency = d.pop("currency", UNSET)

        payment_terms = d.pop("paymentTerms", UNSET)

        due_date = d.pop("dueDate", UNSET)

        customer_line_no = d.pop("customerLineNo", UNSET)

        quote_line_no = d.pop("quoteLineNo", UNSET)

        sow_line_no = d.pop("sowLineNo", UNSET)

        _punchout_ref = d.pop("punchoutRef", UNSET)
        punchout_ref: Union[Unset, PunchoutRefInput]
        if isinstance(_punchout_ref, Unset):
            punchout_ref = UNSET
        else:
            punchout_ref = PunchoutRefInput.from_dict(_punchout_ref)

        _ai = d.pop("ai", UNSET)
        ai: Union[Unset, AiLineScopeInput]
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = AiLineScopeInput.from_dict(_ai)

        line_item_input = cls(
            scope_type=scope_type,
            name=name,
            rule_type=rule_type,
            unit=unit,
            unit_price=unit_price,
            qty=qty,
            nte_amount=nte_amount,
            valid_from=valid_from,
            valid_until=valid_until,
            scope_id=scope_id,
            line_type=line_type,
            currency=currency,
            payment_terms=payment_terms,
            due_date=due_date,
            customer_line_no=customer_line_no,
            quote_line_no=quote_line_no,
            sow_line_no=sow_line_no,
            punchout_ref=punchout_ref,
            ai=ai,
        )

        line_item_input.additional_properties = d
        return line_item_input

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
