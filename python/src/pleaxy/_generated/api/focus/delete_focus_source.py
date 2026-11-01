from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_focus_source_result import DeleteFocusSourceResult
from ...types import Response


def _get_kwargs(
    source_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/focus-sources/{source_id}".format(
            source_id=source_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteFocusSourceResult]:
    if response.status_code == 200:
        response_200 = DeleteFocusSourceResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteFocusSourceResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteFocusSourceResult]:
    """[Buyer] Remove a FOCUS source with the months and AI lines it stored; its connection's own AI read
    resumes. 'edit' on invoices; a signed-in person only.

    Args:
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFocusSourceResult]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteFocusSourceResult]:
    """[Buyer] Remove a FOCUS source with the months and AI lines it stored; its connection's own AI read
    resumes. 'edit' on invoices; a signed-in person only.

    Args:
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFocusSourceResult
    """

    return sync_detailed(
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteFocusSourceResult]:
    """[Buyer] Remove a FOCUS source with the months and AI lines it stored; its connection's own AI read
    resumes. 'edit' on invoices; a signed-in person only.

    Args:
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteFocusSourceResult]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteFocusSourceResult]:
    """[Buyer] Remove a FOCUS source with the months and AI lines it stored; its connection's own AI read
    resumes. 'edit' on invoices; a signed-in person only.

    Args:
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteFocusSourceResult
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            client=client,
        )
    ).parsed
