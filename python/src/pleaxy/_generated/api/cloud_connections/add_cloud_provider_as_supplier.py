from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_cloud_provider_as_supplier_result import (
    AddCloudProviderAsSupplierResult,
)
from ...types import Response


def _get_kwargs(
    provider: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/cloud-connections/{provider}/supplier".format(
            provider=provider,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddCloudProviderAsSupplierResult]:
    if response.status_code == 201:
        response_201 = AddCloudProviderAsSupplierResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddCloudProviderAsSupplierResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddCloudProviderAsSupplierResult]:
    """[Buyer] Add a cloud provider (aws, gcp, azure, oci) to the suppliers list without connecting an
    account - nothing is read from the provider, so nothing is billed in the buyer's cloud account.
    Idempotent: returns the provider's existing supplier row when there is one. Connecting later links
    to the same row. 409 SUPPLIER_ALREADY_LISTED when a supplier with that name already has an
    onboarding under way or approved.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddCloudProviderAsSupplierResult]
    """

    kwargs = _get_kwargs(
        provider=provider,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AddCloudProviderAsSupplierResult]:
    """[Buyer] Add a cloud provider (aws, gcp, azure, oci) to the suppliers list without connecting an
    account - nothing is read from the provider, so nothing is billed in the buyer's cloud account.
    Idempotent: returns the provider's existing supplier row when there is one. Connecting later links
    to the same row. 409 SUPPLIER_ALREADY_LISTED when a supplier with that name already has an
    onboarding under way or approved.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddCloudProviderAsSupplierResult
    """

    return sync_detailed(
        provider=provider,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddCloudProviderAsSupplierResult]:
    """[Buyer] Add a cloud provider (aws, gcp, azure, oci) to the suppliers list without connecting an
    account - nothing is read from the provider, so nothing is billed in the buyer's cloud account.
    Idempotent: returns the provider's existing supplier row when there is one. Connecting later links
    to the same row. 409 SUPPLIER_ALREADY_LISTED when a supplier with that name already has an
    onboarding under way or approved.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddCloudProviderAsSupplierResult]
    """

    kwargs = _get_kwargs(
        provider=provider,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AddCloudProviderAsSupplierResult]:
    """[Buyer] Add a cloud provider (aws, gcp, azure, oci) to the suppliers list without connecting an
    account - nothing is read from the provider, so nothing is billed in the buyer's cloud account.
    Idempotent: returns the provider's existing supplier row when there is one. Connecting later links
    to the same row. 409 SUPPLIER_ALREADY_LISTED when a supplier with that name already has an
    onboarding under way or approved.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddCloudProviderAsSupplierResult
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
        )
    ).parsed
