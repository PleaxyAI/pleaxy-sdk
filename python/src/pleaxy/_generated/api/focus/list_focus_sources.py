from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_focus_sources_result import ListFocusSourcesResult
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/focus-sources",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListFocusSourcesResult]:
    if response.status_code == 200:
        response_200 = ListFocusSourcesResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListFocusSourcesResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ListFocusSourcesResult]:
    """[Buyer] Whether FOCUS import is on, and the workspace's FOCUS sources - uploads, an AWS Data Exports
    FOCUS export, an Azure Cost Management FOCUS export, Google Cloud's FOCUS table, Oracle Cloud's
    FOCUS reports or an S3-compatible bucket - each with its last run (months read, rows, skipped rows
    by reason, or why it failed), the months stored and the most common tag keys. 'view' on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFocusSourcesResult]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListFocusSourcesResult]:
    """[Buyer] Whether FOCUS import is on, and the workspace's FOCUS sources - uploads, an AWS Data Exports
    FOCUS export, an Azure Cost Management FOCUS export, Google Cloud's FOCUS table, Oracle Cloud's
    FOCUS reports or an S3-compatible bucket - each with its last run (months read, rows, skipped rows
    by reason, or why it failed), the months stored and the most common tag keys. 'view' on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListFocusSourcesResult
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ListFocusSourcesResult]:
    """[Buyer] Whether FOCUS import is on, and the workspace's FOCUS sources - uploads, an AWS Data Exports
    FOCUS export, an Azure Cost Management FOCUS export, Google Cloud's FOCUS table, Oracle Cloud's
    FOCUS reports or an S3-compatible bucket - each with its last run (months read, rows, skipped rows
    by reason, or why it failed), the months stored and the most common tag keys. 'view' on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFocusSourcesResult]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListFocusSourcesResult]:
    """[Buyer] Whether FOCUS import is on, and the workspace's FOCUS sources - uploads, an AWS Data Exports
    FOCUS export, an Azure Cost Management FOCUS export, Google Cloud's FOCUS table, Oracle Cloud's
    FOCUS reports or an S3-compatible bucket - each with its last run (months read, rows, skipped rows
    by reason, or why it failed), the months stored and the most common tag keys. 'view' on invoices.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListFocusSourcesResult
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
