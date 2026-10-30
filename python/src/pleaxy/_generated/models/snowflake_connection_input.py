from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnowflakeConnectionInput")


@_attrs_define
class SnowflakeConnectionInput:
    """
    Attributes:
        account (str):
        user (str):
        warehouse (str):
        role (Union[Unset, str]):
    """

    account: str
    user: str
    warehouse: str
    role: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account

        user = self.user

        warehouse = self.warehouse

        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "user": user,
                "warehouse": warehouse,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account = d.pop("account")

        user = d.pop("user")

        warehouse = d.pop("warehouse")

        role = d.pop("role", UNSET)

        snowflake_connection_input = cls(
            account=account,
            user=user,
            warehouse=warehouse,
            role=role,
        )

        snowflake_connection_input.additional_properties = d
        return snowflake_connection_input

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
