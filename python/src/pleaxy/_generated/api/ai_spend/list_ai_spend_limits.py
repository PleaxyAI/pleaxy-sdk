from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_ai_spend_limits_result import ListAiSpendLimitsResult
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/ai-spend/limits",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListAiSpendLimitsResult]:
    if response.status_code == 200:
        response_200 = ListAiSpendLimitsResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListAiSpendLimitsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ListAiSpendLimitsResult]:
    """[Buyer] The limits credentials (one per invoicer, never the key) and each order line's ceiling at
    its provider (amount, month, state, what reading it back gave, every write), and for each connected
    AWS account the values the limits template asks for: Pleaxy's account ID and the connection's
    External ID. 'view' on purchase orders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAiSpendLimitsResult]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListAiSpendLimitsResult]:
    """[Buyer] The limits credentials (one per invoicer, never the key) and each order line's ceiling at
    its provider (amount, month, state, what reading it back gave, every write), and for each connected
    AWS account the values the limits template asks for: Pleaxy's account ID and the connection's
    External ID. 'view' on purchase orders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAiSpendLimitsResult
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ListAiSpendLimitsResult]:
    """[Buyer] The limits credentials (one per invoicer, never the key) and each order line's ceiling at
    its provider (amount, month, state, what reading it back gave, every write), and for each connected
    AWS account the values the limits template asks for: Pleaxy's account ID and the connection's
    External ID. 'view' on purchase orders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAiSpendLimitsResult]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ListAiSpendLimitsResult]:
    """[Buyer] The limits credentials (one per invoicer, never the key) and each order line's ceiling at
    its provider (amount, month, state, what reading it back gave, every write), and for each connected
    AWS account the values the limits template asks for: Pleaxy's account ID and the connection's
    External ID. 'view' on purchase orders.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAiSpendLimitsResult
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
