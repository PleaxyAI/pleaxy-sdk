from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_price_input import CreditPriceInput
    from ..models.databricks_connection_input import DatabricksConnectionInput
    from ..models.snowflake_connection_input import SnowflakeConnectionInput


T = TypeVar("T", bound="CreateAiProviderInput")


@_attrs_define
class CreateAiProviderInput:
    """
    Attributes:
        provider (str):
        key (Union[Unset, str]):
        snowflake (Union[Unset, SnowflakeConnectionInput]):
        databricks (Union[Unset, DatabricksConnectionInput]):
        credit_price (Union[Unset, CreditPriceInput]):
    """

    provider: str
    key: Union[Unset, str] = UNSET
    snowflake: Union[Unset, "SnowflakeConnectionInput"] = UNSET
    databricks: Union[Unset, "DatabricksConnectionInput"] = UNSET
    credit_price: Union[Unset, "CreditPriceInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider

        key = self.key

        snowflake: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.snowflake, Unset):
            snowflake = self.snowflake.to_dict()

        databricks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.databricks, Unset):
            databricks = self.databricks.to_dict()

        credit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credit_price, Unset):
            credit_price = self.credit_price.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if snowflake is not UNSET:
            field_dict["snowflake"] = snowflake
        if databricks is not UNSET:
            field_dict["databricks"] = databricks
        if credit_price is not UNSET:
            field_dict["creditPrice"] = credit_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.credit_price_input import CreditPriceInput
        from ..models.databricks_connection_input import DatabricksConnectionInput
        from ..models.snowflake_connection_input import SnowflakeConnectionInput

        d = src_dict.copy()
        provider = d.pop("provider")

        key = d.pop("key", UNSET)

        _snowflake = d.pop("snowflake", UNSET)
        snowflake: Union[Unset, SnowflakeConnectionInput]
        if isinstance(_snowflake, Unset):
            snowflake = UNSET
        else:
            snowflake = SnowflakeConnectionInput.from_dict(_snowflake)

        _databricks = d.pop("databricks", UNSET)
        databricks: Union[Unset, DatabricksConnectionInput]
        if isinstance(_databricks, Unset):
            databricks = UNSET
        else:
            databricks = DatabricksConnectionInput.from_dict(_databricks)

        _credit_price = d.pop("creditPrice", UNSET)
        credit_price: Union[Unset, CreditPriceInput]
        if isinstance(_credit_price, Unset):
            credit_price = UNSET
        else:
            credit_price = CreditPriceInput.from_dict(_credit_price)

        create_ai_provider_input = cls(
            provider=provider,
            key=key,
            snowflake=snowflake,
            databricks=databricks,
            credit_price=credit_price,
        )

        create_ai_provider_input.additional_properties = d
        return create_ai_provider_input

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
