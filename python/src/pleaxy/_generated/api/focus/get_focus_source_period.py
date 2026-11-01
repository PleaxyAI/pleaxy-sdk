from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_focus_source_period_result import GetFocusSourcePeriodResult
from ...types import Response


def _get_kwargs(
    source_id: str,
    period: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/focus-sources/{source_id}/periods/{period}".format(
            source_id=source_id,
            period=period,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetFocusSourcePeriodResult]:
    if response.status_code == 200:
        response_200 = GetFocusSourcePeriodResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetFocusSourcePeriodResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetFocusSourcePeriodResult]:
    """[Buyer] One stored month of a FOCUS source: totals by currency, each invoice by number (by category
    and service), spend by cost center (from the tag attribution rules) and by issuer. 'view' on
    invoices.

    Args:
        source_id (str):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFocusSourcePeriodResult]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetFocusSourcePeriodResult]:
    """[Buyer] One stored month of a FOCUS source: totals by currency, each invoice by number (by category
    and service), spend by cost center (from the tag attribution rules) and by issuer. 'view' on
    invoices.

    Args:
        source_id (str):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFocusSourcePeriodResult
    """

    return sync_detailed(
        source_id=source_id,
        period=period,
        client=client,
    ).parsed


async def asyncio_detailed(
    source_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetFocusSourcePeriodResult]:
    """[Buyer] One stored month of a FOCUS source: totals by currency, each invoice by number (by category
    and service), spend by cost center (from the tag attribution rules) and by issuer. 'view' on
    invoices.

    Args:
        source_id (str):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFocusSourcePeriodResult]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_id: str,
    period: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetFocusSourcePeriodResult]:
    """[Buyer] One stored month of a FOCUS source: totals by currency, each invoice by number (by category
    and service), spend by cost center (from the tag attribution rules) and by issuer. 'view' on
    invoices.

    Args:
        source_id (str):
        period (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFocusSourcePeriodResult
    """

    return (
        await asyncio_detailed(
            source_id=source_id,
            period=period,
            client=client,
        )
    ).parsed
