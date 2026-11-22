from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ai_commitment_finding import AiCommitmentFinding
    from ..models.cap_finding import CapFinding
    from ..models.commitment_finding import CommitmentFinding
    from ..models.pace_finding import PaceFinding
    from ..models.spike_finding import SpikeFinding
    from ..models.tier_finding import TierFinding
    from ..models.usage_alert_view_body_params import UsageAlertViewBodyParams
    from ..models.usage_alert_view_title_params import UsageAlertViewTitleParams


T = TypeVar("T", bound="UsageAlertView")


@_attrs_define
class UsageAlertView:
    """
    Attributes:
        key (Union[Unset, str]):
        finding (Union['AiCommitmentFinding', 'CapFinding', 'CommitmentFinding', 'PaceFinding', 'SpikeFinding',
            'TierFinding', Unset]):
        title (Union[Unset, str]):
        title_message_id (Union[Unset, str]):
        title_params (Union[Unset, UsageAlertViewTitleParams]):
        body (Union[Unset, str]):
        body_message_id (Union[Unset, str]):
        body_params (Union[Unset, UsageAlertViewBodyParams]):
        sent_at (Union[Unset, str]):
    """

    key: Union[Unset, str] = UNSET
    finding: Union[
        "AiCommitmentFinding",
        "CapFinding",
        "CommitmentFinding",
        "PaceFinding",
        "SpikeFinding",
        "TierFinding",
        Unset,
    ] = UNSET
    title: Union[Unset, str] = UNSET
    title_message_id: Union[Unset, str] = UNSET
    title_params: Union[Unset, "UsageAlertViewTitleParams"] = UNSET
    body: Union[Unset, str] = UNSET
    body_message_id: Union[Unset, str] = UNSET
    body_params: Union[Unset, "UsageAlertViewBodyParams"] = UNSET
    sent_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cap_finding import CapFinding
        from ..models.commitment_finding import CommitmentFinding
        from ..models.pace_finding import PaceFinding
        from ..models.spike_finding import SpikeFinding
        from ..models.tier_finding import TierFinding

        key = self.key

        finding: Union[Dict[str, Any], Unset]
        if isinstance(self.finding, Unset):
            finding = UNSET
        elif isinstance(self.finding, SpikeFinding):
            finding = self.finding.to_dict()
        elif isinstance(self.finding, PaceFinding):
            finding = self.finding.to_dict()
        elif isinstance(self.finding, CapFinding):
            finding = self.finding.to_dict()
        elif isinstance(self.finding, TierFinding):
            finding = self.finding.to_dict()
        elif isinstance(self.finding, CommitmentFinding):
            finding = self.finding.to_dict()
        else:
            finding = self.finding.to_dict()

        title = self.title

        title_message_id = self.title_message_id

        title_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title_params, Unset):
            title_params = self.title_params.to_dict()

        body = self.body

        body_message_id = self.body_message_id

        body_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.body_params, Unset):
            body_params = self.body_params.to_dict()

        sent_at = self.sent_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if finding is not UNSET:
            field_dict["finding"] = finding
        if title is not UNSET:
            field_dict["title"] = title
        if title_message_id is not UNSET:
            field_dict["titleMessageId"] = title_message_id
        if title_params is not UNSET:
            field_dict["titleParams"] = title_params
        if body is not UNSET:
            field_dict["body"] = body
        if body_message_id is not UNSET:
            field_dict["bodyMessageId"] = body_message_id
        if body_params is not UNSET:
            field_dict["bodyParams"] = body_params
        if sent_at is not UNSET:
            field_dict["sentAt"] = sent_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ai_commitment_finding import AiCommitmentFinding
        from ..models.cap_finding import CapFinding
        from ..models.commitment_finding import CommitmentFinding
        from ..models.pace_finding import PaceFinding
        from ..models.spike_finding import SpikeFinding
        from ..models.tier_finding import TierFinding
        from ..models.usage_alert_view_body_params import UsageAlertViewBodyParams
        from ..models.usage_alert_view_title_params import UsageAlertViewTitleParams

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        def _parse_finding(
            data: object,
        ) -> Union[
            "AiCommitmentFinding",
            "CapFinding",
            "CommitmentFinding",
            "PaceFinding",
            "SpikeFinding",
            "TierFinding",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finding_type_0 = SpikeFinding.from_dict(data)

                return finding_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finding_type_1 = PaceFinding.from_dict(data)

                return finding_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finding_type_2 = CapFinding.from_dict(data)

                return finding_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finding_type_3 = TierFinding.from_dict(data)

                return finding_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                finding_type_4 = CommitmentFinding.from_dict(data)

                return finding_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            finding_type_5 = AiCommitmentFinding.from_dict(data)

            return finding_type_5

        finding = _parse_finding(d.pop("finding", UNSET))

        title = d.pop("title", UNSET)

        title_message_id = d.pop("titleMessageId", UNSET)

        _title_params = d.pop("titleParams", UNSET)
        title_params: Union[Unset, UsageAlertViewTitleParams]
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = UsageAlertViewTitleParams.from_dict(_title_params)

        body = d.pop("body", UNSET)

        body_message_id = d.pop("bodyMessageId", UNSET)

        _body_params = d.pop("bodyParams", UNSET)
        body_params: Union[Unset, UsageAlertViewBodyParams]
        if isinstance(_body_params, Unset):
            body_params = UNSET
        else:
            body_params = UsageAlertViewBodyParams.from_dict(_body_params)

        sent_at = d.pop("sentAt", UNSET)

        usage_alert_view = cls(
            key=key,
            finding=finding,
            title=title,
            title_message_id=title_message_id,
            title_params=title_params,
            body=body,
            body_message_id=body_message_id,
            body_params=body_params,
            sent_at=sent_at,
        )

        usage_alert_view.additional_properties = d
        return usage_alert_view

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
