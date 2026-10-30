from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_provider import AiProvider
from ...models.create_ai_provider_input import CreateAiProviderInput
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAiProviderInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/ai-providers",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiProvider]:
    if response.status_code == 201:
        response_201 = AiProvider.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiProvider]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAiProviderInput,
) -> Response[AiProvider]:
    """[Buyer] Connect a direct AI provider whose connector is switched on. OpenAI, Anthropic and Mistral
    take a read-only admin key, checked with one read before anything is saved and then stored KMS-
    encrypted; Snowflake gets a key pair Pleaxy generates, returned pending with its public key to
    assign to the service user (sync then finishes connecting). Seats the provider's pre-created
    supplier row. Counts toward the plan's provider limit. 'create' on suppliers.

    Args:
        body (CreateAiProviderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiProvider]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAiProviderInput,
) -> Optional[AiProvider]:
    """[Buyer] Connect a direct AI provider whose connector is switched on. OpenAI, Anthropic and Mistral
    take a read-only admin key, checked with one read before anything is saved and then stored KMS-
    encrypted; Snowflake gets a key pair Pleaxy generates, returned pending with its public key to
    assign to the service user (sync then finishes connecting). Seats the provider's pre-created
    supplier row. Counts toward the plan's provider limit. 'create' on suppliers.

    Args:
        body (CreateAiProviderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiProvider
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAiProviderInput,
) -> Response[AiProvider]:
    """[Buyer] Connect a direct AI provider whose connector is switched on. OpenAI, Anthropic and Mistral
    take a read-only admin key, checked with one read before anything is saved and then stored KMS-
    encrypted; Snowflake gets a key pair Pleaxy generates, returned pending with its public key to
    assign to the service user (sync then finishes connecting). Seats the provider's pre-created
    supplier row. Counts toward the plan's provider limit. 'create' on suppliers.

    Args:
        body (CreateAiProviderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiProvider]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAiProviderInput,
) -> Optional[AiProvider]:
    """[Buyer] Connect a direct AI provider whose connector is switched on. OpenAI, Anthropic and Mistral
    take a read-only admin key, checked with one read before anything is saved and then stored KMS-
    encrypted; Snowflake gets a key pair Pleaxy generates, returned pending with its public key to
    assign to the service user (sync then finishes connecting). Seats the provider's pre-created
    supplier row. Counts toward the plan's provider limit. 'create' on suppliers.

    Args:
        body (CreateAiProviderInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiProvider
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
