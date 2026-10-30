from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_limit_credential import AiLimitCredential
    from ..models.ai_spend_limit import AiSpendLimit


T = TypeVar("T", bound="ListAiSpendLimitsResult")


@_attrs_define
class ListAiSpendLimitsResult:
    """
    Attributes:
        credentials (Union[Unset, List['AiLimitCredential']]):
        limits (Union[Unset, List['AiSpendLimit']]):
    """

    credentials: Union[Unset, List["AiLimitCredential"]] = UNSET
    limits: Union[Unset, List["AiSpendLimit"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        limits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = []
            for limits_item_data in self.limits:
                limits_item = limits_item_data.to_dict()
                limits.append(limits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_limit_credential import AiLimitCredential
        from ..models.ai_spend_limit import AiSpendLimit

        d = src_dict.copy()
        credentials = []
        _credentials = d.pop("credentials", UNSET)
        for credentials_item_data in _credentials or []:
            credentials_item = AiLimitCredential.from_dict(credentials_item_data)

            credentials.append(credentials_item)

        limits = []
        _limits = d.pop("limits", UNSET)
        for limits_item_data in _limits or []:
            limits_item = AiSpendLimit.from_dict(limits_item_data)

            limits.append(limits_item)

        list_ai_spend_limits_result = cls(
            credentials=credentials,
            limits=limits,
        )

        list_ai_spend_limits_result.additional_properties = d
        return list_ai_spend_limits_result

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
