from typing import Literal, Set, cast

CloudConnectionAzureAgreementType = Literal[
    "EnterpriseAgreement", "MicrosoftCustomerAgreement"
]

CLOUD_CONNECTION_AZURE_AGREEMENT_TYPE_VALUES: Set[CloudConnectionAzureAgreementType] = {
    "EnterpriseAgreement",
    "MicrosoftCustomerAgreement",
}


def check_cloud_connection_azure_agreement_type(
    value: str,
) -> CloudConnectionAzureAgreementType:
    if value in CLOUD_CONNECTION_AZURE_AGREEMENT_TYPE_VALUES:
        return cast(CloudConnectionAzureAgreementType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLOUD_CONNECTION_AZURE_AGREEMENT_TYPE_VALUES!r}"
    )
