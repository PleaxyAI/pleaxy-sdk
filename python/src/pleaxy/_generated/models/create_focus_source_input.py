from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_focus_source_input_kind import (
    CreateFocusSourceInputKind,
    check_create_focus_source_input_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.focus_aws_source_input import FocusAwsSourceInput
    from ..models.focus_azure_source_input import FocusAzureSourceInput
    from ..models.focus_gcp_source_input import FocusGcpSourceInput
    from ..models.focus_oci_source_input import FocusOciSourceInput
    from ..models.focus_s3_compatible_source_input import FocusS3CompatibleSourceInput


T = TypeVar("T", bound="CreateFocusSourceInput")


@_attrs_define
class CreateFocusSourceInput:
    """
    Attributes:
        kind (CreateFocusSourceInputKind):
        label (Union[Unset, str]):
        connection_id (Union[Unset, str]):
        aws (Union[Unset, FocusAwsSourceInput]):
        azure (Union[Unset, FocusAzureSourceInput]):
        gcp (Union[Unset, FocusGcpSourceInput]):
        oci (Union[Unset, FocusOciSourceInput]):
        s3 (Union[Unset, FocusS3CompatibleSourceInput]):
    """

    kind: CreateFocusSourceInputKind
    label: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    aws: Union[Unset, "FocusAwsSourceInput"] = UNSET
    azure: Union[Unset, "FocusAzureSourceInput"] = UNSET
    gcp: Union[Unset, "FocusGcpSourceInput"] = UNSET
    oci: Union[Unset, "FocusOciSourceInput"] = UNSET
    s3: Union[Unset, "FocusS3CompatibleSourceInput"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind: str = self.kind

        label = self.label

        connection_id = self.connection_id

        aws: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws, Unset):
            aws = self.aws.to_dict()

        azure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azure, Unset):
            azure = self.azure.to_dict()

        gcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcp, Unset):
            gcp = self.gcp.to_dict()

        oci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oci, Unset):
            oci = self.oci.to_dict()

        s3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if aws is not UNSET:
            field_dict["aws"] = aws
        if azure is not UNSET:
            field_dict["azure"] = azure
        if gcp is not UNSET:
            field_dict["gcp"] = gcp
        if oci is not UNSET:
            field_dict["oci"] = oci
        if s3 is not UNSET:
            field_dict["s3"] = s3

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.focus_aws_source_input import FocusAwsSourceInput
        from ..models.focus_azure_source_input import FocusAzureSourceInput
        from ..models.focus_gcp_source_input import FocusGcpSourceInput
        from ..models.focus_oci_source_input import FocusOciSourceInput
        from ..models.focus_s3_compatible_source_input import (
            FocusS3CompatibleSourceInput,
        )

        d = src_dict.copy()
        kind = check_create_focus_source_input_kind(d.pop("kind"))

        label = d.pop("label", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        _aws = d.pop("aws", UNSET)
        aws: Union[Unset, FocusAwsSourceInput]
        if isinstance(_aws, Unset):
            aws = UNSET
        else:
            aws = FocusAwsSourceInput.from_dict(_aws)

        _azure = d.pop("azure", UNSET)
        azure: Union[Unset, FocusAzureSourceInput]
        if isinstance(_azure, Unset):
            azure = UNSET
        else:
            azure = FocusAzureSourceInput.from_dict(_azure)

        _gcp = d.pop("gcp", UNSET)
        gcp: Union[Unset, FocusGcpSourceInput]
        if isinstance(_gcp, Unset):
            gcp = UNSET
        else:
            gcp = FocusGcpSourceInput.from_dict(_gcp)

        _oci = d.pop("oci", UNSET)
        oci: Union[Unset, FocusOciSourceInput]
        if isinstance(_oci, Unset):
            oci = UNSET
        else:
            oci = FocusOciSourceInput.from_dict(_oci)

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, FocusS3CompatibleSourceInput]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = FocusS3CompatibleSourceInput.from_dict(_s3)

        create_focus_source_input = cls(
            kind=kind,
            label=label,
            connection_id=connection_id,
            aws=aws,
            azure=azure,
            gcp=gcp,
            oci=oci,
            s3=s3,
        )

        create_focus_source_input.additional_properties = d
        return create_focus_source_input

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
