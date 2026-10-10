from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_supplier_currencies_result_type_1_cloud_provider import (
    SetSupplierCurrenciesResultType1CloudProvider,
    check_set_supplier_currencies_result_type_1_cloud_provider,
)
from ..models.set_supplier_currencies_result_type_1_status import (
    SetSupplierCurrenciesResultType1Status,
    check_set_supplier_currencies_result_type_1_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.late_fee_terms import LateFeeTerms
    from ..models.supplier_region_request import SupplierRegionRequest


T = TypeVar("T", bound="SetSupplierCurrenciesResultType1")


@_attrs_define
class SetSupplierCurrenciesResultType1:
    """
    Attributes:
        id (str):
        buyer_org_id (Union[Unset, str]):
        buyer_name (Union[Unset, str]):
        supplier_org_id (Union[Unset, str]):
        supplier_name (Union[Unset, str]):
        invited_as_name (Union[Unset, str]):
        supplier_contact_email (Union[Unset, str]):
        status (Union[Unset, SetSupplierCurrenciesResultType1Status]):
        questionnaire_template_version (Union[Unset, float]):
        created_at (Union[Unset, str]):
        invited_at (Union[Unset, str]):
        responded_at (Union[Unset, str]):
        reviewed_at (Union[Unset, str]):
        reviewed_by (Union[Unset, str]):
        rejection_reason (Union[Unset, str]):
        cloud_provider (Union[Unset, SetSupplierCurrenciesResultType1CloudProvider]):
        billing_currency (Union[Unset, str]):
        payment_currency (Union[Unset, str]):
        off_platform_invoices_recorded (Union[Unset, bool]):
        supplier_region (Union[Unset, SupplierRegionRequest]):
        accepted_region_name (Union[Unset, str]):
        accepted_region_matches_request (Union[Unset, bool]):
        invoice_feed_enabled (Union[Unset, bool]):
        invoice_feed_updated_at (Union[Unset, str]):
        invoice_feed_updated_by (Union[Unset, str]):
        feed_last_attempt_at (Union[Unset, str]):
        feed_last_accepted_at (Union[Unset, str]):
        feed_accepted_count (Union[Unset, float]):
        feed_last_refused_at (Union[Unset, str]):
        feed_last_refused_code (Union[Unset, str]):
        feed_last_valid_at (Union[Unset, str]):
        feed_valid_count (Union[Unset, float]):
        late_fee_terms (Union[Unset, LateFeeTerms]):
        late_fee_terms_updated_at (Union[Unset, str]):
        late_fee_terms_attested_at (Union[Unset, str]):
        late_fee_terms_attestation_version (Union[Unset, str]):
        questionnaire_redacted (Union[Unset, bool]):
    """

    id: str
    buyer_org_id: Union[Unset, str] = UNSET
    buyer_name: Union[Unset, str] = UNSET
    supplier_org_id: Union[Unset, str] = UNSET
    supplier_name: Union[Unset, str] = UNSET
    invited_as_name: Union[Unset, str] = UNSET
    supplier_contact_email: Union[Unset, str] = UNSET
    status: Union[Unset, SetSupplierCurrenciesResultType1Status] = UNSET
    questionnaire_template_version: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    invited_at: Union[Unset, str] = UNSET
    responded_at: Union[Unset, str] = UNSET
    reviewed_at: Union[Unset, str] = UNSET
    reviewed_by: Union[Unset, str] = UNSET
    rejection_reason: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, SetSupplierCurrenciesResultType1CloudProvider] = UNSET
    billing_currency: Union[Unset, str] = UNSET
    payment_currency: Union[Unset, str] = UNSET
    off_platform_invoices_recorded: Union[Unset, bool] = UNSET
    supplier_region: Union[Unset, "SupplierRegionRequest"] = UNSET
    accepted_region_name: Union[Unset, str] = UNSET
    accepted_region_matches_request: Union[Unset, bool] = UNSET
    invoice_feed_enabled: Union[Unset, bool] = UNSET
    invoice_feed_updated_at: Union[Unset, str] = UNSET
    invoice_feed_updated_by: Union[Unset, str] = UNSET
    feed_last_attempt_at: Union[Unset, str] = UNSET
    feed_last_accepted_at: Union[Unset, str] = UNSET
    feed_accepted_count: Union[Unset, float] = UNSET
    feed_last_refused_at: Union[Unset, str] = UNSET
    feed_last_refused_code: Union[Unset, str] = UNSET
    feed_last_valid_at: Union[Unset, str] = UNSET
    feed_valid_count: Union[Unset, float] = UNSET
    late_fee_terms: Union[Unset, "LateFeeTerms"] = UNSET
    late_fee_terms_updated_at: Union[Unset, str] = UNSET
    late_fee_terms_attested_at: Union[Unset, str] = UNSET
    late_fee_terms_attestation_version: Union[Unset, str] = UNSET
    questionnaire_redacted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        buyer_org_id = self.buyer_org_id

        buyer_name = self.buyer_name

        supplier_org_id = self.supplier_org_id

        supplier_name = self.supplier_name

        invited_as_name = self.invited_as_name

        supplier_contact_email = self.supplier_contact_email

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        questionnaire_template_version = self.questionnaire_template_version

        created_at = self.created_at

        invited_at = self.invited_at

        responded_at = self.responded_at

        reviewed_at = self.reviewed_at

        reviewed_by = self.reviewed_by

        rejection_reason = self.rejection_reason

        cloud_provider: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_provider, Unset):
            cloud_provider = self.cloud_provider

        billing_currency = self.billing_currency

        payment_currency = self.payment_currency

        off_platform_invoices_recorded = self.off_platform_invoices_recorded

        supplier_region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supplier_region, Unset):
            supplier_region = self.supplier_region.to_dict()

        accepted_region_name = self.accepted_region_name

        accepted_region_matches_request = self.accepted_region_matches_request

        invoice_feed_enabled = self.invoice_feed_enabled

        invoice_feed_updated_at = self.invoice_feed_updated_at

        invoice_feed_updated_by = self.invoice_feed_updated_by

        feed_last_attempt_at = self.feed_last_attempt_at

        feed_last_accepted_at = self.feed_last_accepted_at

        feed_accepted_count = self.feed_accepted_count

        feed_last_refused_at = self.feed_last_refused_at

        feed_last_refused_code = self.feed_last_refused_code

        feed_last_valid_at = self.feed_last_valid_at

        feed_valid_count = self.feed_valid_count

        late_fee_terms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.late_fee_terms, Unset):
            late_fee_terms = self.late_fee_terms.to_dict()

        late_fee_terms_updated_at = self.late_fee_terms_updated_at

        late_fee_terms_attested_at = self.late_fee_terms_attested_at

        late_fee_terms_attestation_version = self.late_fee_terms_attestation_version

        questionnaire_redacted = self.questionnaire_redacted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if buyer_org_id is not UNSET:
            field_dict["buyerOrgId"] = buyer_org_id
        if buyer_name is not UNSET:
            field_dict["buyerName"] = buyer_name
        if supplier_org_id is not UNSET:
            field_dict["supplierOrgId"] = supplier_org_id
        if supplier_name is not UNSET:
            field_dict["supplierName"] = supplier_name
        if invited_as_name is not UNSET:
            field_dict["invitedAsName"] = invited_as_name
        if supplier_contact_email is not UNSET:
            field_dict["supplierContactEmail"] = supplier_contact_email
        if status is not UNSET:
            field_dict["status"] = status
        if questionnaire_template_version is not UNSET:
            field_dict["questionnaireTemplateVersion"] = questionnaire_template_version
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if invited_at is not UNSET:
            field_dict["invitedAt"] = invited_at
        if responded_at is not UNSET:
            field_dict["respondedAt"] = responded_at
        if reviewed_at is not UNSET:
            field_dict["reviewedAt"] = reviewed_at
        if reviewed_by is not UNSET:
            field_dict["reviewedBy"] = reviewed_by
        if rejection_reason is not UNSET:
            field_dict["rejectionReason"] = rejection_reason
        if cloud_provider is not UNSET:
            field_dict["cloudProvider"] = cloud_provider
        if billing_currency is not UNSET:
            field_dict["billingCurrency"] = billing_currency
        if payment_currency is not UNSET:
            field_dict["paymentCurrency"] = payment_currency
        if off_platform_invoices_recorded is not UNSET:
            field_dict["offPlatformInvoicesRecorded"] = off_platform_invoices_recorded
        if supplier_region is not UNSET:
            field_dict["supplierRegion"] = supplier_region
        if accepted_region_name is not UNSET:
            field_dict["acceptedRegionName"] = accepted_region_name
        if accepted_region_matches_request is not UNSET:
            field_dict["acceptedRegionMatchesRequest"] = accepted_region_matches_request
        if invoice_feed_enabled is not UNSET:
            field_dict["invoiceFeedEnabled"] = invoice_feed_enabled
        if invoice_feed_updated_at is not UNSET:
            field_dict["invoiceFeedUpdatedAt"] = invoice_feed_updated_at
        if invoice_feed_updated_by is not UNSET:
            field_dict["invoiceFeedUpdatedBy"] = invoice_feed_updated_by
        if feed_last_attempt_at is not UNSET:
            field_dict["feedLastAttemptAt"] = feed_last_attempt_at
        if feed_last_accepted_at is not UNSET:
            field_dict["feedLastAcceptedAt"] = feed_last_accepted_at
        if feed_accepted_count is not UNSET:
            field_dict["feedAcceptedCount"] = feed_accepted_count
        if feed_last_refused_at is not UNSET:
            field_dict["feedLastRefusedAt"] = feed_last_refused_at
        if feed_last_refused_code is not UNSET:
            field_dict["feedLastRefusedCode"] = feed_last_refused_code
        if feed_last_valid_at is not UNSET:
            field_dict["feedLastValidAt"] = feed_last_valid_at
        if feed_valid_count is not UNSET:
            field_dict["feedValidCount"] = feed_valid_count
        if late_fee_terms is not UNSET:
            field_dict["lateFeeTerms"] = late_fee_terms
        if late_fee_terms_updated_at is not UNSET:
            field_dict["lateFeeTermsUpdatedAt"] = late_fee_terms_updated_at
        if late_fee_terms_attested_at is not UNSET:
            field_dict["lateFeeTermsAttestedAt"] = late_fee_terms_attested_at
        if late_fee_terms_attestation_version is not UNSET:
            field_dict["lateFeeTermsAttestationVersion"] = (
                late_fee_terms_attestation_version
            )
        if questionnaire_redacted is not UNSET:
            field_dict["questionnaireRedacted"] = questionnaire_redacted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.late_fee_terms import LateFeeTerms
        from ..models.supplier_region_request import SupplierRegionRequest

        d = src_dict.copy()
        id = d.pop("id")

        buyer_org_id = d.pop("buyerOrgId", UNSET)

        buyer_name = d.pop("buyerName", UNSET)

        supplier_org_id = d.pop("supplierOrgId", UNSET)

        supplier_name = d.pop("supplierName", UNSET)

        invited_as_name = d.pop("invitedAsName", UNSET)

        supplier_contact_email = d.pop("supplierContactEmail", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SetSupplierCurrenciesResultType1Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_set_supplier_currencies_result_type_1_status(_status)

        questionnaire_template_version = d.pop("questionnaireTemplateVersion", UNSET)

        created_at = d.pop("createdAt", UNSET)

        invited_at = d.pop("invitedAt", UNSET)

        responded_at = d.pop("respondedAt", UNSET)

        reviewed_at = d.pop("reviewedAt", UNSET)

        reviewed_by = d.pop("reviewedBy", UNSET)

        rejection_reason = d.pop("rejectionReason", UNSET)

        _cloud_provider = d.pop("cloudProvider", UNSET)
        cloud_provider: Union[Unset, SetSupplierCurrenciesResultType1CloudProvider]
        if isinstance(_cloud_provider, Unset):
            cloud_provider = UNSET
        else:
            cloud_provider = check_set_supplier_currencies_result_type_1_cloud_provider(
                _cloud_provider
            )

        billing_currency = d.pop("billingCurrency", UNSET)

        payment_currency = d.pop("paymentCurrency", UNSET)

        off_platform_invoices_recorded = d.pop("offPlatformInvoicesRecorded", UNSET)

        _supplier_region = d.pop("supplierRegion", UNSET)
        supplier_region: Union[Unset, SupplierRegionRequest]
        if isinstance(_supplier_region, Unset):
            supplier_region = UNSET
        else:
            supplier_region = SupplierRegionRequest.from_dict(_supplier_region)

        accepted_region_name = d.pop("acceptedRegionName", UNSET)

        accepted_region_matches_request = d.pop("acceptedRegionMatchesRequest", UNSET)

        invoice_feed_enabled = d.pop("invoiceFeedEnabled", UNSET)

        invoice_feed_updated_at = d.pop("invoiceFeedUpdatedAt", UNSET)

        invoice_feed_updated_by = d.pop("invoiceFeedUpdatedBy", UNSET)

        feed_last_attempt_at = d.pop("feedLastAttemptAt", UNSET)

        feed_last_accepted_at = d.pop("feedLastAcceptedAt", UNSET)

        feed_accepted_count = d.pop("feedAcceptedCount", UNSET)

        feed_last_refused_at = d.pop("feedLastRefusedAt", UNSET)

        feed_last_refused_code = d.pop("feedLastRefusedCode", UNSET)

        feed_last_valid_at = d.pop("feedLastValidAt", UNSET)

        feed_valid_count = d.pop("feedValidCount", UNSET)

        _late_fee_terms = d.pop("lateFeeTerms", UNSET)
        late_fee_terms: Union[Unset, LateFeeTerms]
        if isinstance(_late_fee_terms, Unset):
            late_fee_terms = UNSET
        else:
            late_fee_terms = LateFeeTerms.from_dict(_late_fee_terms)

        late_fee_terms_updated_at = d.pop("lateFeeTermsUpdatedAt", UNSET)

        late_fee_terms_attested_at = d.pop("lateFeeTermsAttestedAt", UNSET)

        late_fee_terms_attestation_version = d.pop(
            "lateFeeTermsAttestationVersion", UNSET
        )

        questionnaire_redacted = d.pop("questionnaireRedacted", UNSET)

        set_supplier_currencies_result_type_1 = cls(
            id=id,
            buyer_org_id=buyer_org_id,
            buyer_name=buyer_name,
            supplier_org_id=supplier_org_id,
            supplier_name=supplier_name,
            invited_as_name=invited_as_name,
            supplier_contact_email=supplier_contact_email,
            status=status,
            questionnaire_template_version=questionnaire_template_version,
            created_at=created_at,
            invited_at=invited_at,
            responded_at=responded_at,
            reviewed_at=reviewed_at,
            reviewed_by=reviewed_by,
            rejection_reason=rejection_reason,
            cloud_provider=cloud_provider,
            billing_currency=billing_currency,
            payment_currency=payment_currency,
            off_platform_invoices_recorded=off_platform_invoices_recorded,
            supplier_region=supplier_region,
            accepted_region_name=accepted_region_name,
            accepted_region_matches_request=accepted_region_matches_request,
            invoice_feed_enabled=invoice_feed_enabled,
            invoice_feed_updated_at=invoice_feed_updated_at,
            invoice_feed_updated_by=invoice_feed_updated_by,
            feed_last_attempt_at=feed_last_attempt_at,
            feed_last_accepted_at=feed_last_accepted_at,
            feed_accepted_count=feed_accepted_count,
            feed_last_refused_at=feed_last_refused_at,
            feed_last_refused_code=feed_last_refused_code,
            feed_last_valid_at=feed_last_valid_at,
            feed_valid_count=feed_valid_count,
            late_fee_terms=late_fee_terms,
            late_fee_terms_updated_at=late_fee_terms_updated_at,
            late_fee_terms_attested_at=late_fee_terms_attested_at,
            late_fee_terms_attestation_version=late_fee_terms_attestation_version,
            questionnaire_redacted=questionnaire_redacted,
        )

        set_supplier_currencies_result_type_1.additional_properties = d
        return set_supplier_currencies_result_type_1

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
