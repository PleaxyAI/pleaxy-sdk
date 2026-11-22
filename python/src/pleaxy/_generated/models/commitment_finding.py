from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commitment_finding_type import (
    CommitmentFindingType,
    check_commitment_finding_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommitmentFinding")


@_attrs_define
class CommitmentFinding:
    """
    Attributes:
        type (Union[Unset, CommitmentFindingType]):
        committed (Union[Unset, float]):
        billed (Union[Unset, float]):
        projected (Union[Unset, float]):
        total (Union[Unset, float]):
        window_start (Union[Unset, str]):
        window_end (Union[Unset, str]):
        excess (Union[Unset, float]):
        contract_id (Union[Unset, str]):
        contract_title (Union[Unset, str]):
        supplier (Union[Unset, str]):
        currency (Union[Unset, str]):
    """

    type: Union[Unset, CommitmentFindingType] = UNSET
    committed: Union[Unset, float] = UNSET
    billed: Union[Unset, float] = UNSET
    projected: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    window_start: Union[Unset, str] = UNSET
    window_end: Union[Unset, str] = UNSET
    excess: Union[Unset, float] = UNSET
    contract_id: Union[Unset, str] = UNSET
    contract_title: Union[Unset, str] = UNSET
    supplier: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        committed = self.committed

        billed = self.billed

        projected = self.projected

        total = self.total

        window_start = self.window_start

        window_end = self.window_end

        excess = self.excess

        contract_id = self.contract_id

        contract_title = self.contract_title

        supplier = self.supplier

        currency = self.currency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if committed is not UNSET:
            field_dict["committed"] = committed
        if billed is not UNSET:
            field_dict["billed"] = billed
        if projected is not UNSET:
            field_dict["projected"] = projected
        if total is not UNSET:
            field_dict["total"] = total
        if window_start is not UNSET:
            field_dict["windowStart"] = window_start
        if window_end is not UNSET:
            field_dict["windowEnd"] = window_end
        if excess is not UNSET:
            field_dict["excess"] = excess
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if contract_title is not UNSET:
            field_dict["contractTitle"] = contract_title
        if supplier is not UNSET:
            field_dict["supplier"] = supplier
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, CommitmentFindingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_commitment_finding_type(_type)

        committed = d.pop("committed", UNSET)

        billed = d.pop("billed", UNSET)

        projected = d.pop("projected", UNSET)

        total = d.pop("total", UNSET)

        window_start = d.pop("windowStart", UNSET)

        window_end = d.pop("windowEnd", UNSET)

        excess = d.pop("excess", UNSET)

        contract_id = d.pop("contractId", UNSET)

        contract_title = d.pop("contractTitle", UNSET)

        supplier = d.pop("supplier", UNSET)

        currency = d.pop("currency", UNSET)

        commitment_finding = cls(
            type=type,
            committed=committed,
            billed=billed,
            projected=projected,
            total=total,
            window_start=window_start,
            window_end=window_end,
            excess=excess,
            contract_id=contract_id,
            contract_title=contract_title,
            supplier=supplier,
            currency=currency,
        )

        commitment_finding.additional_properties = d
        return commitment_finding

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
