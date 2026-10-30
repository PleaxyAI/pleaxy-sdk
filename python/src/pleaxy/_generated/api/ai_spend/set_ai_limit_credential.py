from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ai_limit_credential import AiLimitCredential
from ...models.set_ai_limit_credential_input import SetAiLimitCredentialInput
from ...types import Response


def _get_kwargs(
    invoicer_id: str,
    *,
    body: SetAiLimitCredentialInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/ai-spend/limit-credentials/{invoicer_id}".format(
            invoicer_id=invoicer_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AiLimitCredential]:
    if response.status_code == 200:
        response_200 = AiLimitCredential.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AiLimitCredential]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiLimitCredentialInput,
) -> Response[AiLimitCredential]:
    """[Buyer] The separate write credential for one invoicer's ceilings - an AWS limits role, a Google
    Cloud limits service account, an Azure limits app, or an OpenAI or Anthropic admin key - checked
    with one read before it is saved. Never the read-only connection's. Logged-in users only, 'edit' on
    suppliers.

    Args:
        invoicer_id (str):
        body (SetAiLimitCredentialInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiLimitCredential]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiLimitCredentialInput,
) -> Optional[AiLimitCredential]:
    """[Buyer] The separate write credential for one invoicer's ceilings - an AWS limits role, a Google
    Cloud limits service account, an Azure limits app, or an OpenAI or Anthropic admin key - checked
    with one read before it is saved. Never the read-only connection's. Logged-in users only, 'edit' on
    suppliers.

    Args:
        invoicer_id (str):
        body (SetAiLimitCredentialInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiLimitCredential
    """

    return sync_detailed(
        invoicer_id=invoicer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiLimitCredentialInput,
) -> Response[AiLimitCredential]:
    """[Buyer] The separate write credential for one invoicer's ceilings - an AWS limits role, a Google
    Cloud limits service account, an Azure limits app, or an OpenAI or Anthropic admin key - checked
    with one read before it is saved. Never the read-only connection's. Logged-in users only, 'edit' on
    suppliers.

    Args:
        invoicer_id (str):
        body (SetAiLimitCredentialInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AiLimitCredential]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetAiLimitCredentialInput,
) -> Optional[AiLimitCredential]:
    """[Buyer] The separate write credential for one invoicer's ceilings - an AWS limits role, a Google
    Cloud limits service account, an Azure limits app, or an OpenAI or Anthropic admin key - checked
    with one read before it is saved. Never the read-only connection's. Logged-in users only, 'edit' on
    suppliers.

    Args:
        invoicer_id (str):
        body (SetAiLimitCredentialInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AiLimitCredential
    """

    return (
        await asyncio_detailed(
            invoicer_id=invoicer_id,
            client=client,
            body=body,
        )
    ).parsed
