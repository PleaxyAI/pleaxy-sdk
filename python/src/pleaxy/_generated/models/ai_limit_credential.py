from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_limit_credential_invoicer import (
    AiLimitCredentialInvoicer,
    check_ai_limit_credential_invoicer,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_limit_credential_aws import AiLimitCredentialAws
    from ..models.ai_limit_credential_azure import AiLimitCredentialAzure
    from ..models.ai_limit_credential_gcp import AiLimitCredentialGcp


T = TypeVar("T", bound="AiLimitCredential")


@_attrs_define
class AiLimitCredential:
    """
    Attributes:
        invoicer_id (Union[Unset, str]):
        invoicer (Union[Unset, AiLimitCredentialInvoicer]):
        aws (Union[Unset, AiLimitCredentialAws]):
        gcp (Union[Unset, AiLimitCredentialGcp]):
        azure (Union[Unset, AiLimitCredentialAzure]):
        key_hint (Union[Unset, str]):
        notify_email (Union[Unset, str]):
        created_at (Union[Unset, str]):
        created_by (Union[Unset, str]):
    """

    invoicer_id: Union[Unset, str] = UNSET
    invoicer: Union[Unset, AiLimitCredentialInvoicer] = UNSET
    aws: Union[Unset, "AiLimitCredentialAws"] = UNSET
    gcp: Union[Unset, "AiLimitCredentialGcp"] = UNSET
    azure: Union[Unset, "AiLimitCredentialAzure"] = UNSET
    key_hint: Union[Unset, str] = UNSET
    notify_email: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoicer_id = self.invoicer_id

        invoicer: Union[Unset, str] = UNSET
        if not isinstance(self.invoicer, Unset):
            invoicer = self.invoicer

        aws: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        gcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        azure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        key_hint = self.key_hint

        notify_email = self.notify_email

        created_at = self.created_at

        created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoicer_id is not UNSET:
            field_dict["invoicerId"] = invoicer_id
        if invoicer is not UNSET:
            field_dict["invoicer"] = invoicer
        if aws is not UNSET:
            field_dict["aws"] = aws
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if azure is not UNSET:
            field_dict["azure"] = azure
        if key_hint is not UNSET:
            field_dict["keyHint"] = key_hint
        if notify_email is not UNSET:
            field_dict["notifyEmail"] = notify_email
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_limit_credential_aws import AiLimitCredentialAws
        from ..models.ai_limit_credential_azure import AiLimitCredentialAzure
        from ..models.ai_limit_credential_gcp import AiLimitCredentialGcp

        d = src_dict.copy()
        invoicer_id = d.pop("invoicerId", UNSET)

        _invoicer = d.pop("invoicer", UNSET)
        invoicer: Union[Unset, AiLimitCredentialInvoicer]
        if isinstance(_invoicer, Unset):
            invoicer = UNSET
        else:
            invoicer = check_ai_limit_credential_invoicer(_invoicer)

        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, AiLimitCredentialAws]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = AiLimitCredentialAws.from_dict(_aws)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, AiLimitCredentialGcp]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = AiLimitCredentialGcp.from_dict(_gcp)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, AiLimitCredentialAzure]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = AiLimitCredentialAzure.from_dict(_azure)

        key_hint = d.pop("keyHint", UNSET)

        notify_email = d.pop("notifyEmail", UNSET)

        created_at = d.pop("createdAt", UNSET)

        created_by = d.pop("createdBy", UNSET)

        ai_limit_credential = cls(
            invoicer_id=invoicer_id,
            invoicer=invoicer,
            aws=aws,
            gcp=gcp,
            azure=azure,
            key_hint=key_hint,
            notify_email=notify_email,
            created_at=created_at,
            created_by=created_by,
        )

        ai_limit_credential.additional_properties = d
        return ai_limit_credential

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
