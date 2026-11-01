from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.focus_source_view_kind import (
    FocusSourceViewKind,
    check_focus_source_view_kind,
)
from ..models.focus_source_view_provider import (
    FocusSourceViewProvider,
    check_focus_source_view_provider,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_run import FocusRun
    from ..models.focus_source_view_aws import FocusSourceViewAws
    from ..models.focus_source_view_azure import FocusSourceViewAzure
    from ..models.focus_source_view_gcp import FocusSourceViewGcp
    from ..models.focus_source_view_oci import FocusSourceViewOci
    from ..models.focus_source_view_s3 import FocusSourceViewS3
    from ..models.provider_commitment import ProviderCommitment


T = TypeVar("T", bound="FocusSourceView")


@_attrs_define
class FocusSourceView:
    """
    Attributes:
        id (str):
        s3 (Union[Unset, FocusSourceViewS3]):
        aws (Union[Unset, FocusSourceViewAws]):
        gcp (Union[Unset, FocusSourceViewGcp]):
        azure (Union[Unset, FocusSourceViewAzure]):
        oci (Union[Unset, FocusSourceViewOci]):
        provider (Union[Unset, FocusSourceViewProvider]):
        created_at (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        kind (Union[Unset, FocusSourceViewKind]):
        label (Union[Unset, str]):
        connection_id (Union[Unset, str]):
        periods (Union[Unset, List[str]]):
        last_run (Union[Unset, FocusRun]):
        tag_keys (Union[Unset, List[str]]):
        commitments (Union[Unset, List['ProviderCommitment']]):
    """

    id: str
    s3: Union[Unset, "FocusSourceViewS3"] = UNSET
    aws: Union[Unset, "FocusSourceViewAws"] = UNSET
    gcp: Union[Unset, "FocusSourceViewGcp"] = UNSET
    azure: Union[Unset, "FocusSourceViewAzure"] = UNSET
    oci: Union[Unset, "FocusSourceViewOci"] = UNSET
    provider: Union[Unset, FocusSourceViewProvider] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    kind: Union[Unset, FocusSourceViewKind] = UNSET
    label: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    periods: Union[Unset, List[str]] = UNSET
    last_run: Union[Unset, "FocusRun"] = UNSET
    tag_keys: Union[Unset, List[str]] = UNSET
    commitments: Union[Unset, List["ProviderCommitment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        s3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        aws: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        gcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        azure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        oci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oci, Unset):
            oci = self.oci.to_dict()

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        created_at = self.created_at

        updated_at = self.updated_at

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        label = self.label

        connection_id = self.connection_id

        periods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = self.periods

        last_run: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.to_dict()

        tag_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tag_keys, Unset):
            tag_keys = self.tag_keys

        commitments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commitments, Unset):
            commitments = []
            for commitments_item_data in self.commitments:
                commitments_item = commitments_item_data.to_dict()
                commitments.append(commitments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if aws is not UNSET:
            field_dict["aws"] = aws
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if azure is not UNSET:
            field_dict["azure"] = azure
        if oci is not UNSET:
            field_dict["oci"] = oci
        if provider is not UNSET:
            field_dict["provider"] = provider
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if periods is not UNSET:
            field_dict["periods"] = periods
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if tag_keys is not UNSET:
            field_dict["tagKeys"] = tag_keys
        if commitments is not UNSET:
            field_dict["commitments"] = commitments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_run import FocusRun
        from ..models.focus_source_view_aws import FocusSourceViewAws
        from ..models.focus_source_view_azure import FocusSourceViewAzure
        from ..models.focus_source_view_gcp import FocusSourceViewGcp
        from ..models.focus_source_view_oci import FocusSourceViewOci
        from ..models.focus_source_view_s3 import FocusSourceViewS3
        from ..models.provider_commitment import ProviderCommitment

        d = src_dict.copy()
        id = d.pop("id")

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, FocusSourceViewS3]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = FocusSourceViewS3.from_dict(_s3)

        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, FocusSourceViewAws]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = FocusSourceViewAws.from_dict(_aws)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, FocusSourceViewGcp]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = FocusSourceViewGcp.from_dict(_gcp)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, FocusSourceViewAzure]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = FocusSourceViewAzure.from_dict(_azure)

        _oci = d.pop("oci", UNSET)
        oci: Union[Unset, FocusSourceViewOci]
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = FocusSourceViewOci.from_dict(_oci)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, FocusSourceViewProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_focus_source_view_provider(_provider)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, FocusSourceViewKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_focus_source_view_kind(_kind)

        label = d.pop("label", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        periods = cast(List[str], d.pop("periods", UNSET))

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, FocusRun]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = FocusRun.from_dict(_last_run)

        tag_keys = cast(List[str], d.pop("tagKeys", UNSET))

        commitments = []
        _commitments = d.pop("commitments", UNSET)
        for commitments_item_data in _commitments or []:
            commitments_item = ProviderCommitment.from_dict(commitments_item_data)

            commitments.append(commitments_item)

        focus_source_view = cls(
            id=id,
            s3=s3,
            aws=aws,
            gcp=gcp,
            azure=azure,
            oci=oci,
            provider=provider,
            created_at=created_at,
            updated_at=updated_at,
            kind=kind,
            label=label,
            connection_id=connection_id,
            periods=periods,
            last_run=last_run,
            tag_keys=tag_keys,
            commitments=commitments,
        )

        focus_source_view.additional_properties = d
        return focus_source_view

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
