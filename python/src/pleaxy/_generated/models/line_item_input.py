from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_item_input_rule_type import (
    LineItemInputRuleType,
    check_line_item_input_rule_type,
)
from ..models.line_item_input_scope_type import (
    LineItemInputScopeType,
    check_line_item_input_scope_type,
)
from ..types import UNSET, Unset

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
        payment_terms (str):
        valid_from (str):
        valid_until (str):
        scope_id (Union[None, Unset, str]):
        currency (Union[Unset, str]): ISO 4217. Optional - the server writes the order's currency on every line. If
            sent, it must be the order's currency (any case); another currency is a 400, since Pleaxy doesn't convert
            currencies.
        customer_line_no (Union[Unset, str]): The buyer's own number for this line (e.g. from their ERP), up to 40
            characters. Optional, like poNumber; stored and shown alongside the server's lineNo, never replacing it.
        quote_line_no (Union[Unset, float]): The line of the order's quote (quoteImportId) this line was filled from,
            when Pleaxy read the quote. Kept on the line; the app shows the line as priced from the supplier's quote unless
            a contract rate priced it.
    """

    scope_type: LineItemInputScopeType
    name: str
    rule_type: LineItemInputRuleType
    unit: str
    unit_price: float
    qty: float
    nte_amount: float
    payment_terms: str
    valid_from: str
    valid_until: str
    scope_id: Union[None, Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    customer_line_no: Union[Unset, str] = UNSET
    quote_line_no: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scope_type: str = self.scope_type

        name = self.name

        rule_type: str = self.rule_type

        unit = self.unit

        unit_price = self.unit_price

        qty = self.qty

        nte_amount = self.nte_amount

        payment_terms = self.payment_terms

        valid_from = self.valid_from

        valid_until = self.valid_until

        scope_id: Union[None, Unset, str]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        currency = self.currency

        customer_line_no = self.customer_line_no

        quote_line_no = self.quote_line_no

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
                "paymentTerms": payment_terms,
                "validFrom": valid_from,
                "validUntil": valid_until,
            }
        )
        if scope_id is not UNSET:
            field_dict["scopeId"] = scope_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if customer_line_no is not UNSET:
            field_dict["customerLineNo"] = customer_line_no
        if quote_line_no is not UNSET:
            field_dict["quoteLineNo"] = quote_line_no

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        scope_type = check_line_item_input_scope_type(d.pop("scopeType"))

        name = d.pop("name")

        rule_type = check_line_item_input_rule_type(d.pop("ruleType"))

        unit = d.pop("unit")

        unit_price = d.pop("unitPrice")

        qty = d.pop("qty")

        nte_amount = d.pop("nteAmount")

        payment_terms = d.pop("paymentTerms")

        valid_from = d.pop("validFrom")

        valid_until = d.pop("validUntil")

        def _parse_scope_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_id = _parse_scope_id(d.pop("scopeId", UNSET))

        currency = d.pop("currency", UNSET)

        customer_line_no = d.pop("customerLineNo", UNSET)

        quote_line_no = d.pop("quoteLineNo", UNSET)

        line_item_input = cls(
            scope_type=scope_type,
            name=name,
            rule_type=rule_type,
            unit=unit,
            unit_price=unit_price,
            qty=qty,
            nte_amount=nte_amount,
            payment_terms=payment_terms,
            valid_from=valid_from,
            valid_until=valid_until,
            scope_id=scope_id,
            currency=currency,
            customer_line_no=customer_line_no,
            quote_line_no=quote_line_no,
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
