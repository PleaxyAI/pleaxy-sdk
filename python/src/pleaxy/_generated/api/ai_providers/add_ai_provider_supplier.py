from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_ai_provider_supplier_result import AddAiProviderSupplierResult
from ...types import Response


def _get_kwargs(
    provider: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ai-providers/{provider}/supplier".format(
            provider=provider,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddAiProviderSupplierResult]:
    if response.status_code == 201:
        response_201 = AddAiProviderSupplierResult.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddAiProviderSupplierResult]:
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
) -> Response[AddAiProviderSupplierResult]:
    """[Buyer] Add an AI invoicer (openai, anthropic, mistral, cohere, xai, openrouter, snowflake,
    databricks, coreweave, lambda, nebius, crusoe) to the suppliers list without connecting: its pre-
    created supplier row, pending invite. Idempotent; connecting later links to the same row. 409
    SUPPLIER_ALREADY_LISTED when a supplier of that name already has a relationship under way. 'create'
    on suppliers.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAiProviderSupplierResult]
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
) -> Optional[AddAiProviderSupplierResult]:
    """[Buyer] Add an AI invoicer (openai, anthropic, mistral, cohere, xai, openrouter, snowflake,
    databricks, coreweave, lambda, nebius, crusoe) to the suppliers list without connecting: its pre-
    created supplier row, pending invite. Idempotent; connecting later links to the same row. 409
    SUPPLIER_ALREADY_LISTED when a supplier of that name already has a relationship under way. 'create'
    on suppliers.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAiProviderSupplierResult
    """

    return sync_detailed(
        provider=provider,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AddAiProviderSupplierResult]:
    """[Buyer] Add an AI invoicer (openai, anthropic, mistral, cohere, xai, openrouter, snowflake,
    databricks, coreweave, lambda, nebius, crusoe) to the suppliers list without connecting: its pre-
    created supplier row, pending invite. Idempotent; connecting later links to the same row. 409
    SUPPLIER_ALREADY_LISTED when a supplier of that name already has a relationship under way. 'create'
    on suppliers.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAiProviderSupplierResult]
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
) -> Optional[AddAiProviderSupplierResult]:
    """[Buyer] Add an AI invoicer (openai, anthropic, mistral, cohere, xai, openrouter, snowflake,
    databricks, coreweave, lambda, nebius, crusoe) to the suppliers list without connecting: its pre-
    created supplier row, pending invite. Idempotent; connecting later links to the same row. 409
    SUPPLIER_ALREADY_LISTED when a supplier of that name already has a relationship under way. 'create'
    on suppliers.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAiProviderSupplierResult
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
        )
    ).parsed
