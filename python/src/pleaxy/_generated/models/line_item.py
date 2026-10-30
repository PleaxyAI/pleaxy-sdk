from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_item_line_type import LineItemLineType, check_line_item_line_type
from ..models.line_item_price_source import (
    LineItemPriceSource,
    check_line_item_price_source,
)
from ..models.line_item_rule_type import LineItemRuleType, check_line_item_rule_type
from ..models.line_item_scope_type import LineItemScopeType, check_line_item_scope_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_line_scope import AiLineScope
    from ..models.line_item_punchout_ref import LineItemPunchoutRef
    from ..models.punchout_line_origin import PunchoutLineOrigin


T = TypeVar("T", bound="LineItem")


@_attrs_define
class LineItem:
    """
    Attributes:
        line_no (Union[Unset, float]):
        line_type (Union[Unset, LineItemLineType]):
        scope_type (Union[Unset, LineItemScopeType]):
        scope_id (Union[None, Unset, str]):
        name (Union[Unset, str]):
        rule_type (Union[Unset, LineItemRuleType]):
        unit (Union[Unset, str]):
        unit_price (Union[Unset, float]):
        qty (Union[Unset, float]):
        nte_amount (Union[Unset, float]):
        currency (Union[Unset, str]):
        payment_terms (Union[Unset, str]):
        valid_from (Union[Unset, str]):
        valid_until (Union[Unset, str]):
        due_date (Union[Unset, str]):
        consumed (Union[Unset, float]):
        supplier_sku (Union[Unset, str]):
        price_source (Union[Unset, LineItemPriceSource]):
        customer_line_no (Union[Unset, str]):
        contract_id (Union[Unset, str]):
        contract_term_id (Union[Unset, str]):
        quote_line_no (Union[Unset, float]):
        sow_line_no (Union[Unset, float]):
        origin (Union[Unset, PunchoutLineOrigin]):
        punchout_ref (Union[Unset, LineItemPunchoutRef]):
        ai (Union[Unset, AiLineScope]):
    """

    line_no: Union[Unset, float] = UNSET
    line_type: Union[Unset, LineItemLineType] = UNSET
    scope_type: Union[Unset, LineItemScopeType] = UNSET
    scope_id: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    rule_type: Union[Unset, LineItemRuleType] = UNSET
    unit: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    qty: Union[Unset, float] = UNSET
    nte_amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    payment_terms: Union[Unset, str] = UNSET
    valid_from: Union[Unset, str] = UNSET
    valid_until: Union[Unset, str] = UNSET
    due_date: Union[Unset, str] = UNSET
    consumed: Union[Unset, float] = UNSET
    supplier_sku: Union[Unset, str] = UNSET
    price_source: Union[Unset, LineItemPriceSource] = UNSET
    customer_line_no: Union[Unset, str] = UNSET
    contract_id: Union[Unset, str] = UNSET
    contract_term_id: Union[Unset, str] = UNSET
    quote_line_no: Union[Unset, float] = UNSET
    sow_line_no: Union[Unset, float] = UNSET
    origin: Union[Unset, "PunchoutLineOrigin"] = UNSET
    punchout_ref: Union[Unset, "LineItemPunchoutRef"] = UNSET
    ai: Union[Unset, "AiLineScope"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no

        line_type: Union[Unset, str] = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type

        scope_type: Union[Unset, str] = UNSET
        if not isinstance(self.scope_type, Unset):
            scope_type = self.scope_type

        scope_id: Union[None, Unset, str]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        name = self.name

        rule_type: Union[Unset, str] = UNSET
        if not isinstance(self.rule_type, Unset):
            rule_type = self.rule_type

        unit = self.unit

        unit_price = self.unit_price

        qty = self.qty

        nte_amount = self.nte_amount

        currency = self.currency

        payment_terms = self.payment_terms

        valid_from = self.valid_from

        valid_until = self.valid_until

        due_date = self.due_date

        consumed = self.consumed

        supplier_sku = self.supplier_sku

        price_source: Union[Unset, str] = UNSET
        if not isinstance(self.price_source, Unset):
            price_source = self.price_source

        customer_line_no = self.customer_line_no

        contract_id = self.contract_id

        contract_term_id = self.contract_term_id

        quote_line_no = self.quote_line_no

        sow_line_no = self.sow_line_no

        origin: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        punchout_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.punchout_ref, Unset):
            punchout_ref = self.punchout_ref.to_dict()

        ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if scope_type is not UNSET:
            field_dict["scopeType"] = scope_type
        if scope_id is not UNSET:
            field_dict["scopeId"] = scope_id
        if name is not UNSET:
            field_dict["name"] = name
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if qty is not UNSET:
            field_dict["qty"] = qty
        if nte_amount is not UNSET:
            field_dict["nteAmount"] = nte_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if consumed is not UNSET:
            field_dict["consumed"] = consumed
        if supplier_sku is not UNSET:
            field_dict["supplierSku"] = supplier_sku
        if price_source is not UNSET:
            field_dict["priceSource"] = price_source
        if customer_line_no is not UNSET:
            field_dict["customerLineNo"] = customer_line_no
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_term_id is not UNSET:
            field_dict["contractTermId"] = contract_term_id
        if quote_line_no is not UNSET:
            field_dict["quoteLineNo"] = quote_line_no
        if sow_line_no is not UNSET:
            field_dict["sowLineNo"] = sow_line_no
        if origin is not UNSET:
            field_dict["origin"] = origin
        if punchout_ref is not UNSET:
            field_dict["punchoutRef"] = punchout_ref
        if ai is not UNSET:
            field_dict["ai"] = ai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_line_scope import AiLineScope
        from ..models.line_item_punchout_ref import LineItemPunchoutRef
        from ..models.punchout_line_origin import PunchoutLineOrigin

        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: Union[Unset, LineItemLineType]
        if isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = check_line_item_line_type(_line_type)

        _scope_type = d.pop("scopeType", UNSET)
        scope_type: Union[Unset, LineItemScopeType]
        if isinstance(_scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = check_line_item_scope_type(_scope_type)

        def _parse_scope_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_id = _parse_scope_id(d.pop("scopeId", UNSET))

        name = d.pop("name", UNSET)

        _rule_type = d.pop("ruleType", UNSET)
        rule_type: Union[Unset, LineItemRuleType]
        if isinstance(_rule_type, Unset):
            rule_type = UNSET
        else:
            rule_type = check_line_item_rule_type(_rule_type)

        unit = d.pop("unit", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        qty = d.pop("qty", UNSET)

        nte_amount = d.pop("nteAmount", UNSET)

        currency = d.pop("currency", UNSET)

        payment_terms = d.pop("paymentTerms", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_until = d.pop("validUntil", UNSET)

        due_date = d.pop("dueDate", UNSET)

        consumed = d.pop("consumed", UNSET)

        supplier_sku = d.pop("supplierSku", UNSET)

        _price_source = d.pop("priceSource", UNSET)
        price_source: Union[Unset, LineItemPriceSource]
        if isinstance(_price_source, Unset):
            price_source = UNSET
        else:
            price_source = check_line_item_price_source(_price_source)

        customer_line_no = d.pop("customerLineNo", UNSET)

        contract_id = d.pop("contractId", UNSET)

        contract_term_id = d.pop("contractTermId", UNSET)

        quote_line_no = d.pop("quoteLineNo", UNSET)

        sow_line_no = d.pop("sowLineNo", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, PunchoutLineOrigin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = PunchoutLineOrigin.from_dict(_origin)

        _punchout_ref = d.pop("punchoutRef", UNSET)
        punchout_ref: Union[Unset, LineItemPunchoutRef]
        if isinstance(_punchout_ref, Unset):
            punchout_ref = UNSET
        else:
            punchout_ref = LineItemPunchoutRef.from_dict(_punchout_ref)

        _ai = d.pop("ai", UNSET)
        ai: Union[Unset, AiLineScope]
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = AiLineScope.from_dict(_ai)

        line_item = cls(
            line_no=line_no,
            line_type=line_type,
            scope_type=scope_type,
            scope_id=scope_id,
            name=name,
            rule_type=rule_type,
            unit=unit,
            unit_price=unit_price,
            qty=qty,
            nte_amount=nte_amount,
            currency=currency,
            payment_terms=payment_terms,
            valid_from=valid_from,
            valid_until=valid_until,
            due_date=due_date,
            consumed=consumed,
            supplier_sku=supplier_sku,
            price_source=price_source,
            customer_line_no=customer_line_no,
            contract_id=contract_id,
            contract_term_id=contract_term_id,
            quote_line_no=quote_line_no,
            sow_line_no=sow_line_no,
            origin=origin,
            punchout_ref=punchout_ref,
            ai=ai,
        )

        line_item.additional_properties = d
        return line_item

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
