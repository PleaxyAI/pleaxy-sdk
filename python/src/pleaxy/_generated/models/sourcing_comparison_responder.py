from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sourcing_comparison_responder_answered_via import (
    SourcingComparisonResponderAnsweredVia,
    check_sourcing_comparison_responder_answered_via,
)
from ..models.sourcing_comparison_responder_onboarding import (
    SourcingComparisonResponderOnboarding,
    check_sourcing_comparison_responder_onboarding,
)
from ..models.sourcing_comparison_responder_risk_level import (
    SourcingComparisonResponderRiskLevel,
    check_sourcing_comparison_responder_risk_level,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sourcing_attachment import SourcingAttachment
    from ..models.sourcing_comparison_responder_evaluation import (
        SourcingComparisonResponderEvaluation,
    )
    from ..models.sourcing_weighted_score import SourcingWeightedScore


T = TypeVar("T", bound="SourcingComparisonResponder")


@_attrs_define
class SourcingComparisonResponder:
    """
    Attributes:
        supplier_key (Union[Unset, str]):
        supplier_connection_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        total (Union[None, Unset, float]):
        complete (Union[Unset, bool]):
        lowest_total (Union[Unset, bool]):
        longest_lead_time_days (Union[None, Unset, float]):
        meets_needed_by (Union[None, Unset, bool]):
        payment_terms_days (Union[Unset, float]):
        valid_until (Union[Unset, str]):
        reference (Union[Unset, str]):
        note (Union[Unset, str]):
        quote_import_id (Union[Unset, str]):
        attachments (Union[Unset, List['SourcingAttachment']]):
        submitted_at (Union[Unset, str]):
        version (Union[Unset, float]):
        answered_via (Union[Unset, SourcingComparisonResponderAnsweredVia]):
        answered_by_email (Union[Unset, str]):
        risk_level (Union[Unset, SourcingComparisonResponderRiskLevel]):
        onboarding (Union[Unset, SourcingComparisonResponderOnboarding]):
        score (Union[None, Unset, float]):
        score_complete (Union[Unset, bool]):
        carried_from (Union[Unset, float]):
        weighted (Union[Unset, SourcingWeightedScore]):
        evaluation (Union[Unset, SourcingComparisonResponderEvaluation]):
    """

    supplier_key: Union[Unset, str] = UNSET
    supplier_connection_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    total: Union[None, Unset, float] = UNSET
    complete: Union[Unset, bool] = UNSET
    lowest_total: Union[Unset, bool] = UNSET
    longest_lead_time_days: Union[None, Unset, float] = UNSET
    meets_needed_by: Union[None, Unset, bool] = UNSET
    payment_terms_days: Union[Unset, float] = UNSET
    valid_until: Union[Unset, str] = UNSET
    reference: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    quote_import_id: Union[Unset, str] = UNSET
    attachments: Union[Unset, List["SourcingAttachment"]] = UNSET
    submitted_at: Union[Unset, str] = UNSET
    version: Union[Unset, float] = UNSET
    answered_via: Union[Unset, SourcingComparisonResponderAnsweredVia] = UNSET
    answered_by_email: Union[Unset, str] = UNSET
    risk_level: Union[Unset, SourcingComparisonResponderRiskLevel] = UNSET
    onboarding: Union[Unset, SourcingComparisonResponderOnboarding] = UNSET
    score: Union[None, Unset, float] = UNSET
    score_complete: Union[Unset, bool] = UNSET
    carried_from: Union[Unset, float] = UNSET
    weighted: Union[Unset, "SourcingWeightedScore"] = UNSET
    evaluation: Union[Unset, "SourcingComparisonResponderEvaluation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        supplier_key = self.supplier_key

        supplier_connection_id = self.supplier_connection_id

        supplier_name = self.supplier_name

        total: Union[None, Unset, float]
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        complete = self.complete

        lowest_total = self.lowest_total

        longest_lead_time_days: Union[None, Unset, float]
        if isinstance(self.longest_lead_time_days, Unset):
            longest_lead_time_days = UNSET
        else:
            longest_lead_time_days = self.longest_lead_time_days

        meets_needed_by: Union[None, Unset, bool]
        if isinstance(self.meets_needed_by, Unset):
            meets_needed_by = UNSET
        else:
            meets_needed_by = self.meets_needed_by

        payment_terms_days = self.payment_terms_days

        valid_until = self.valid_until

        reference = self.reference

        note = self.note

        quote_import_id = self.quote_import_id

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        submitted_at = self.submitted_at

        version = self.version

        answered_via: Union[Unset, str] = UNSET
        if not isinstance(self.answered_via, Unset):
            answered_via = self.answered_via

        answered_by_email = self.answered_by_email

        risk_level: Union[Unset, str] = UNSET
        if not isinstance(self.risk_level, Unset):
            risk_level = self.risk_level

        onboarding: Union[Unset, str] = UNSET
        if not isinstance(self.onboarding, Unset):
            onboarding = self.onboarding

        score: Union[None, Unset, float]
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        score_complete = self.score_complete

        carried_from = self.carried_from

        weighted: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.weighted, Unset):
            weighted = self.weighted.to_dict()

        evaluation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.evaluation, Unset):
            evaluation = self.evaluation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if supplier_key is not UNSET:
            field_dict["supplierKey"] = supplier_key
        if supplier_connection_id is not UNSET:
            field_dict["supplierConnectionId"] = supplier_connection_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if total is not UNSET:
            field_dict["total"] = total
        if complete is not UNSET:
            field_dict["complete"] = complete
        if lowest_total is not UNSET:
            field_dict["lowestTotal"] = lowest_total
        if longest_lead_time_days is not UNSET:
            field_dict["longestLeadTimeDays"] = longest_lead_time_days
        if meets_needed_by is not UNSET:
            field_dict["meetsNeededBy"] = meets_needed_by
        if payment_terms_days is not UNSET:
            field_dict["paymentTermsDays"] = payment_terms_days
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if reference is not UNSET:
            field_dict["reference"] = reference
        if note is not UNSET:
            field_dict["note"] = note
        if quote_import_id is not UNSET:
            field_dict["quoteImportId"] = quote_import_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if submitted_at is not UNSET:
            field_dict["submittedAt"] = submitted_at
        if version is not UNSET:
            field_dict["version"] = version
        if answered_via is not UNSET:
            field_dict["answeredVia"] = answered_via
        if answered_by_email is not UNSET:
            field_dict["answeredByEmail"] = answered_by_email
        if risk_level is not UNSET:
            field_dict["riskLevel"] = risk_level
        if onboarding is not UNSET:
            field_dict["onboarding"] = onboarding
        if score is not UNSET:
            field_dict["score"] = score
        if score_complete is not UNSET:
            field_dict["scoreComplete"] = score_complete
        if carried_from is not UNSET:
            field_dict["carriedFrom"] = carried_from
        if weighted is not UNSET:
            field_dict["weighted"] = weighted
        if evaluation is not UNSET:
            field_dict["evaluation"] = evaluation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sourcing_attachment import SourcingAttachment
        from ..models.sourcing_comparison_responder_evaluation import (
            SourcingComparisonResponderEvaluation,
        )
        from ..models.sourcing_weighted_score import SourcingWeightedScore

        d = src_dict.copy()
        supplier_key = d.pop("supplierKey", UNSET)

        supplier_connection_id = d.pop("supplierConnectionId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        def _parse_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total = _parse_total(d.pop("total", UNSET))

        complete = d.pop("complete", UNSET)

        lowest_total = d.pop("lowestTotal", UNSET)

        def _parse_longest_lead_time_days(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longest_lead_time_days = _parse_longest_lead_time_days(
            d.pop("longestLeadTimeDays", UNSET)
        )

        def _parse_meets_needed_by(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        meets_needed_by = _parse_meets_needed_by(d.pop("meetsNeededBy", UNSET))

        payment_terms_days = d.pop("paymentTermsDays", UNSET)

        valid_until = d.pop("validUntil", UNSET)

        reference = d.pop("reference", UNSET)

        note = d.pop("note", UNSET)

        quote_import_id = d.pop("quoteImportId", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = SourcingAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        submitted_at = d.pop("submittedAt", UNSET)

        version = d.pop("version", UNSET)

        _answered_via = d.pop("answeredVia", UNSET)
        answered_via: Union[Unset, SourcingComparisonResponderAnsweredVia]
        if isinstance(_answered_via, Unset):
            answered_via = UNSET
        else:
            answered_via = check_sourcing_comparison_responder_answered_via(
                _answered_via
            )

        answered_by_email = d.pop("answeredByEmail", UNSET)

        _risk_level = d.pop("riskLevel", UNSET)
        risk_level: Union[Unset, SourcingComparisonResponderRiskLevel]
        if isinstance(_risk_level, Unset):
            risk_level = UNSET
        else:
            risk_level = check_sourcing_comparison_responder_risk_level(_risk_level)

        _onboarding = d.pop("onboarding", UNSET)
        onboarding: Union[Unset, SourcingComparisonResponderOnboarding]
        if isinstance(_onboarding, Unset):
            onboarding = UNSET
        else:
            onboarding = check_sourcing_comparison_responder_onboarding(_onboarding)

        def _parse_score(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        score = _parse_score(d.pop("score", UNSET))

        score_complete = d.pop("scoreComplete", UNSET)

        carried_from = d.pop("carriedFrom", UNSET)

        _weighted = d.pop("weighted", UNSET)
        weighted: Union[Unset, SourcingWeightedScore]
        if isinstance(_weighted, Unset):
            weighted = UNSET
        else:
            weighted = SourcingWeightedScore.from_dict(_weighted)

        _evaluation = d.pop("evaluation", UNSET)
        evaluation: Union[Unset, SourcingComparisonResponderEvaluation]
        if isinstance(_evaluation, Unset):
            evaluation = UNSET
        else:
            evaluation = SourcingComparisonResponderEvaluation.from_dict(_evaluation)

        sourcing_comparison_responder = cls(
            supplier_key=supplier_key,
            supplier_connection_id=supplier_connection_id,
            supplier_name=supplier_name,
            total=total,
            complete=complete,
            lowest_total=lowest_total,
            longest_lead_time_days=longest_lead_time_days,
            meets_needed_by=meets_needed_by,
            payment_terms_days=payment_terms_days,
            valid_until=valid_until,
            reference=reference,
            note=note,
            quote_import_id=quote_import_id,
            attachments=attachments,
            submitted_at=submitted_at,
            version=version,
            answered_via=answered_via,
            answered_by_email=answered_by_email,
            risk_level=risk_level,
            onboarding=onboarding,
            score=score,
            score_complete=score_complete,
            carried_from=carried_from,
            weighted=weighted,
            evaluation=evaluation,
        )

        sourcing_comparison_responder.additional_properties = d
        return sourcing_comparison_responder

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
