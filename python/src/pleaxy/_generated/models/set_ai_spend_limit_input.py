from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAiSpendLimitInput")


@_attrs_define
class SetAiSpendLimitInput:
    """
    Attributes:
        invoicer_id (str): The invoicer the order covers: a cloud connection or AI provider id with a limits credential.
        target (Union[Unset, str]): OpenAI: the project (proj_...). Anthropic: the workspace (wrkspc_...). Google Cloud:
            the project id, for a spend cap.
        deny (Union[Unset, bool]): Stop spend at the ceiling where the provider can (default true); false only alerts.
    """

    invoicer_id: str
    target: Union[Unset, str] = UNSET
    deny: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        target = self.target

        deny = self.deny

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoicerId": invoicer_id,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target
        if deny is not UNSET:
            field_dict["deny"] = deny

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId")

        target = d.pop("target", UNSET)

        deny = d.pop("deny", UNSET)

        set_ai_spend_limit_input = cls(
            invoicer_id=invoicer_id,
            target=target,
            deny=deny,
        )

        set_ai_spend_limit_input.additional_properties = d
        return set_ai_spend_limit_input

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
