from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAiSpendLimitsResultAwsSetupItem")


@_attrs_define
class ListAiSpendLimitsResultAwsSetupItem:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        pleaxy_account_id (Union[Unset, str]):
        external_id (Union[Unset, str]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    pleaxy_account_id: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        pleaxy_account_id = self.pleaxy_account_id

        external_id = self.external_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if pleaxy_account_id is not UNSET:
            field_dict["pleaxyAccountId"] = pleaxy_account_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        pleaxy_account_id = d.pop("pleaxyAccountId", UNSET)

        external_id = d.pop("externalId", UNSET)

        list_ai_spend_limits_result_aws_setup_item = cls(
            invoicer_id=invoicer_id,
            pleaxy_account_id=pleaxy_account_id,
            external_id=external_id,
        )

        list_ai_spend_limits_result_aws_setup_item.additional_properties = d
        return list_ai_spend_limits_result_aws_setup_item

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
