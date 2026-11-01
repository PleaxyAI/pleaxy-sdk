from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderCommitment")


@_attrs_define
class ProviderCommitment:
    """
    Attributes:
        id (str):
        contract_id (Union[Unset, str]):
        category (Union[Unset, str]):
        type (Union[Unset, str]):
        description (Union[Unset, str]):
        issuer (Union[Unset, str]):
        provider (Union[Unset, str]):
        period_start (Union[Unset, str]):
        period_end (Union[Unset, str]):
        cost (Union[Unset, float]):
        currency (Union[Unset, str]):
        quantity (Union[Unset, float]):
        unit (Union[Unset, str]):
        status (Union[Unset, str]):
    """

    id: str
    contract_id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    period_start: Union[Unset, str] = UNSET
    period_end: Union[Unset, str] = UNSET
    cost: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    unit: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        contract_id = self.contract_id

        category = self.category

        type = self.type

        description = self.description

        issuer = self.issuer

        provider = self.provider

        period_start = self.period_start

        period_end = self.period_end

        cost = self.cost

        currency = self.currency

        quantity = self.quantity

        unit = self.unit

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if category is not UNSET:
            field_dict["category"] = category
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if provider is not UNSET:
            field_dict["provider"] = provider
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if cost is not UNSET:
            field_dict["cost"] = cost
        if currency is not UNSET:
            field_dict["currency"] = currency
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if unit is not UNSET:
            field_dict["unit"] = unit
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        contract_id = d.pop("contractId", UNSET)

        category = d.pop("category", UNSET)

        type = d.pop("type", UNSET)

        description = d.pop("description", UNSET)

        issuer = d.pop("issuer", UNSET)

        provider = d.pop("provider", UNSET)

        period_start = d.pop("periodStart", UNSET)

        period_end = d.pop("periodEnd", UNSET)

        cost = d.pop("cost", UNSET)

        currency = d.pop("currency", UNSET)

        quantity = d.pop("quantity", UNSET)

        unit = d.pop("unit", UNSET)

        status = d.pop("status", UNSET)

        provider_commitment = cls(
            id=id,
            contract_id=contract_id,
            category=category,
            type=type,
            description=description,
            issuer=issuer,
            provider=provider,
            period_start=period_start,
            period_end=period_end,
            cost=cost,
            currency=currency,
            quantity=quantity,
            unit=unit,
            status=status,
        )

        provider_commitment.additional_properties = d
        return provider_commitment

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
