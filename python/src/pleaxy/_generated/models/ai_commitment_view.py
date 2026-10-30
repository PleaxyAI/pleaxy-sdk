from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_commitment_view_kind import (
    AiCommitmentViewKind,
    check_ai_commitment_view_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_commitment_view_ai import AiCommitmentViewAi


T = TypeVar("T", bound="AiCommitmentView")


@_attrs_define
class AiCommitmentView:
    """
    Attributes:
        kind (Union[Unset, AiCommitmentViewKind]):
        contract_id (Union[Unset, str]):
        contract_title (Union[Unset, str]):
        term_id (Union[Unset, str]):
        po_id (Union[Unset, str]):
        line_no (Union[Unset, float]):
        supplier (Union[Unset, str]):
        description (Union[Unset, str]):
        ai (Union[Unset, AiCommitmentViewAi]):
        currency (Union[Unset, str]):
        term_start (Union[Unset, str]):
        term_end (Union[Unset, str]):
        committed (Union[Unset, float]):
        used (Union[Unset, float]):
        remaining (Union[Unset, float]):
        used_pct (Union[Unset, float]):
        projected (Union[Unset, float]):
        unit (Union[Unset, str]):
    """

    kind: Union[Unset, AiCommitmentViewKind] = UNSET
    contract_id: Union[Unset, str] = UNSET
    contract_title: Union[Unset, str] = UNSET
    term_id: Union[Unset, str] = UNSET
    po_id: Union[Unset, str] = UNSET
    line_no: Union[Unset, float] = UNSET
    supplier: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    ai: Union[Unset, "AiCommitmentViewAi"] = UNSET
    currency: Union[Unset, str] = UNSET
    term_start: Union[Unset, str] = UNSET
    term_end: Union[Unset, str] = UNSET
    committed: Union[Unset, float] = UNSET
    used: Union[Unset, float] = UNSET
    remaining: Union[Unset, float] = UNSET
    used_pct: Union[Unset, float] = UNSET
    projected: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        contract_id = self.contract_id

        contract_title = self.contract_title

        term_id = self.term_id

        po_id = self.po_id

        line_no = self.line_no

        supplier = self.supplier

        description = self.description

        ai: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ai, Unset):
            ai = self.ai.to_dict()

        currency = self.currency

        term_start = self.term_start

        term_end = self.term_end

        committed = self.committed

        used = self.used

        remaining = self.remaining

        used_pct = self.used_pct

        projected = self.projected

        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_title is not UNSET:
            field_dict["contractTitle"] = contract_title
        if term_id is not UNSET:
            field_dict["termId"] = term_id
        if po_id is not UNSET:
            field_dict["poId"] = po_id
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if description is not UNSET:
            field_dict["description"] = description
        if ai is not UNSET:
            field_dict["ai"] = ai
        if currency is not UNSET:
            field_dict["currency"] = currency
        if term_start is not UNSET:
            field_dict["termStart"] = term_start
        if term_end is not UNSET:
            field_dict["termEnd"] = term_end
        if committed is not UNSET:
            field_dict["committed"] = committed
        if used is not UNSET:
            field_dict["used"] = used
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if used_pct is not UNSET:
            field_dict["usedPct"] = used_pct
        if projected is not UNSET:
            field_dict["projected"] = projected
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_commitment_view_ai import AiCommitmentViewAi

        d = src_dict.copy()
        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, AiCommitmentViewKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_ai_commitment_view_kind(_kind)

        contract_id = d.pop("contractId", UNSET)

        contract_title = d.pop("contractTitle", UNSET)

        term_id = d.pop("termId", UNSET)

        po_id = d.pop("poId", UNSET)

        line_no = d.pop("lineNo", UNSET)

        supplier = d.pop("supplier", UNSET)

        description = d.pop("description", UNSET)

        _ai = d.pop("ai", UNSET)
        ai: Union[Unset, AiCommitmentViewAi]
        if isinstance(_ai, Unset):
            ai = UNSET
        else:
            ai = AiCommitmentViewAi.from_dict(_ai)

        currency = d.pop("currency", UNSET)

        term_start = d.pop("termStart", UNSET)

        term_end = d.pop("termEnd", UNSET)

        committed = d.pop("committed", UNSET)

        used = d.pop("used", UNSET)

        remaining = d.pop("remaining", UNSET)

        used_pct = d.pop("usedPct", UNSET)

        projected = d.pop("projected", UNSET)

        unit = d.pop("unit", UNSET)

        ai_commitment_view = cls(
            kind=kind,
            contract_id=contract_id,
            contract_title=contract_title,
            term_id=term_id,
            po_id=po_id,
            line_no=line_no,
            supplier=supplier,
            description=description,
            ai=ai,
            currency=currency,
            term_start=term_start,
            term_end=term_end,
            committed=committed,
            used=used,
            remaining=remaining,
            used_pct=used_pct,
            projected=projected,
            unit=unit,
        )

        ai_commitment_view.additional_properties = d
        return ai_commitment_view

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
