from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_access_removal_action import (
    InvoiceAccessRemovalAction,
    check_invoice_access_removal_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_access_regrant import InvoiceAccessRegrant
    from ..models.invoice_access_removal_sso_mapping_saved import (
        InvoiceAccessRemovalSsoMappingSaved,
    )


T = TypeVar("T", bound="InvoiceAccessRemoval")


@_attrs_define
class InvoiceAccessRemoval:
    """
    Attributes:
        at (Union[Unset, str]):
        action (Union[Unset, InvoiceAccessRemovalAction]):
        by_key (Union[Unset, str]):
        by_name (Union[Unset, str]):
        by_sso (Union[Unset, bool]):
        target_key (Union[Unset, str]):
        target_name (Union[Unset, str]):
        sso_mapping_saved (Union[Unset, InvoiceAccessRemovalSsoMappingSaved]):
        regained (Union[Unset, InvoiceAccessRegrant]):
    """

    at: Union[Unset, str] = UNSET
    action: Union[Unset, InvoiceAccessRemovalAction] = UNSET
    by_key: Union[Unset, str] = UNSET
    by_name: Union[Unset, str] = UNSET
    by_sso: Union[Unset, bool] = UNSET
    target_key: Union[Unset, str] = UNSET
    target_name: Union[Unset, str] = UNSET
    sso_mapping_saved: Union[Unset, "InvoiceAccessRemovalSsoMappingSaved"] = UNSET
    regained: Union[Unset, "InvoiceAccessRegrant"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        at = self.at

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action

        by_key = self.by_key

        by_name = self.by_name

        by_sso = self.by_sso

        target_key = self.target_key

        target_name = self.target_name

        sso_mapping_saved: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sso_mapping_saved, Unset):
            sso_mapping_saved = self.sso_mapping_saved.to_dict()

        regained: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.regained, Unset):
            regained = self.regained.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if at is not UNSET:
            field_dict["at"] = at
        if action is not UNSET:
            field_dict["action"] = action
        if by_key is not UNSET:
            field_dict["byKey"] = by_key
        if by_name is not UNSET:
            field_dict["byName"] = by_name
        if by_sso is not UNSET:
            field_dict["bySso"] = by_sso
        if target_key is not UNSET:
            field_dict["targetKey"] = target_key
        if target_name is not UNSET:
            field_dict["targetName"] = target_name
        if sso_mapping_saved is not UNSET:
            field_dict["ssoMappingSaved"] = sso_mapping_saved
        if regained is not UNSET:
            field_dict["regained"] = regained

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_access_regrant import InvoiceAccessRegrant
        from ..models.invoice_access_removal_sso_mapping_saved import (
            InvoiceAccessRemovalSsoMappingSaved,
        )

        d = src_dict.copy()
        at = d.pop("at", UNSET)

        _action = d.pop("action", UNSET)
        action: Union[Unset, InvoiceAccessRemovalAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = check_invoice_access_removal_action(_action)

        by_key = d.pop("byKey", UNSET)

        by_name = d.pop("byName", UNSET)

        by_sso = d.pop("bySso", UNSET)

        target_key = d.pop("targetKey", UNSET)

        target_name = d.pop("targetName", UNSET)

        _sso_mapping_saved = d.pop("ssoMappingSaved", UNSET)
        sso_mapping_saved: Union[Unset, InvoiceAccessRemovalSsoMappingSaved]
        if isinstance(_sso_mapping_saved, Unset):
            sso_mapping_saved = UNSET
        else:
            sso_mapping_saved = InvoiceAccessRemovalSsoMappingSaved.from_dict(
                _sso_mapping_saved
            )

        _regained = d.pop("regained", UNSET)
        regained: Union[Unset, InvoiceAccessRegrant]
        if isinstance(_regained, Unset):
            regained = UNSET
        else:
            regained = InvoiceAccessRegrant.from_dict(_regained)

        invoice_access_removal = cls(
            at=at,
            action=action,
            by_key=by_key,
            by_name=by_name,
            by_sso=by_sso,
            target_key=target_key,
            target_name=target_name,
            sso_mapping_saved=sso_mapping_saved,
            regained=regained,
        )

        invoice_access_removal.additional_properties = d
        return invoice_access_removal

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
