from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_award_order import SourcingAwardOrder, check_sourcing_award_order
from ..models.sourcing_award_outcome import (
    SourcingAwardOutcome,
    check_sourcing_award_outcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_award_line import SourcingAwardLine


T = TypeVar("T", bound="SourcingAward")


@_attrs_define
class SourcingAward:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        supplier_connection_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        reason (Union[Unset, str]):
        total (Union[Unset, float]):
        currency (Union[Unset, str]):
        lines (Union[Unset, List['SourcingAwardLine']]):
        awarded_at (Union[Unset, str]):
        awarded_by (Union[Unset, str]):
        order (Union[Unset, SourcingAwardOrder]):
        po_id (Union[Unset, str]):
        quote_import_id (Union[Unset, str]):
        outcome (Union[Unset, SourcingAwardOutcome]):
        contract_id (Union[Unset, str]):
    """

    supplier_key: Union[Unset, str] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    total: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    lines: Union[Unset, List["SourcingAwardLine"]] = UNSET
    awarded_at: Union[Unset, str] = UNSET
    awarded_by: Union[Unset, str] = UNSET
    order: Union[Unset, SourcingAwardOrder] = UNSET
    po_id: Union[Unset, str] = UNSET
    quote_import_id: Union[Unset, str] = UNSET
    outcome: Union[Unset, SourcingAwardOutcome] = UNSET
    contract_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        supplier_connection_id = self.supplier_connection_id

        supplier_name = self.supplier_name

        reason = self.reason

        total = self.total

        currency = self.currency

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        awarded_at = self.awarded_at

        awarded_by = self.awarded_by

        order: Union[Unset, str] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order

        po_id = self.po_id

        quote_import_id = self.quote_import_id

        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        contract_id = self.contract_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if total is not UNSET:
            field_dict["total"] = total
        if currency is not UNSET:
            field_dict["currency"] = currency
        if lines is not UNSET:
            field_dict["lines"] = lines
        if awarded_at is not UNSET:
            field_dict["awardedAt"] = awarded_at
        if awarded_by is not UNSET:
            field_dict["awardedBy"] = awarded_by
        if order is not UNSET:
            field_dict["order"] = order
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_award_line import SourcingAwardLine

        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        reason = d.pop("reason", UNSET)

        total = d.pop("total", UNSET)

        currency = d.pop("currency", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = SourcingAwardLine.from_dict(lines_item_data)

            lines.append(lines_item)

        awarded_at = d.pop("awardedAt", UNSET)

        awarded_by = d.pop("awardedBy", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, SourcingAwardOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = check_sourcing_award_order(_order)

        po_id = d.pop("poId", UNSET)

        quote_import_id = d.pop("quoteImportId", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, SourcingAwardOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_sourcing_award_outcome(_outcome)

        contract_id = d.pop("contractId", UNSET)

        sourcing_award = cls(
            supplier_key=supplier_key,
            supplier_connection_id=supplier_connection_id,
            supplier_name=supplier_name,
            reason=reason,
            total=total,
            currency=currency,
            lines=lines,
            awarded_at=awarded_at,
            awarded_by=awarded_by,
            order=order,
            po_id=po_id,
            quote_import_id=quote_import_id,
            outcome=outcome,
            contract_id=contract_id,
        )

        sourcing_award.additional_properties = d
        return sourcing_award

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
