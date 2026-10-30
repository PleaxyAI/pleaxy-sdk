from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_ai_limit_credential_result import RemoveAiLimitCredentialResult
from ...types import Response


def _get_kwargs(
    invoicer_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/ai-spend/limit-credentials/{invoicer_id}".format(
            invoicer_id=invoicer_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemoveAiLimitCredentialResult]:
    if response.status_code == 200:
        response_200 = RemoveAiLimitCredentialResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoveAiLimitCredentialResult]:
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
) -> Response[RemoveAiLimitCredentialResult]:
    """[Buyer] Removes an invoicer's limits credential: Pleaxy sets no more ceilings there; the read-only
    connection stays as it was. Remove the role or key at the provider too. Logged-in users only, 'edit'
    on suppliers.

    Args:
        invoicer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveAiLimitCredentialResult]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveAiLimitCredentialResult]:
    """[Buyer] Removes an invoicer's limits credential: Pleaxy sets no more ceilings there; the read-only
    connection stays as it was. Remove the role or key at the provider too. Logged-in users only, 'edit'
    on suppliers.

    Args:
        invoicer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveAiLimitCredentialResult
    """

    return sync_detailed(
        invoicer_id=invoicer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RemoveAiLimitCredentialResult]:
    """[Buyer] Removes an invoicer's limits credential: Pleaxy sets no more ceilings there; the read-only
    connection stays as it was. Remove the role or key at the provider too. Logged-in users only, 'edit'
    on suppliers.

    Args:
        invoicer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveAiLimitCredentialResult]
    """

    kwargs = _get_kwargs(
        invoicer_id=invoicer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoicer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveAiLimitCredentialResult]:
    """[Buyer] Removes an invoicer's limits credential: Pleaxy sets no more ceilings there; the read-only
    connection stays as it was. Remove the role or key at the provider too. Logged-in users only, 'edit'
    on suppliers.

    Args:
        invoicer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveAiLimitCredentialResult
    """

    return (
        await asyncio_detailed(
            invoicer_id=invoicer_id,
            client=client,
        )
    ).parsed
