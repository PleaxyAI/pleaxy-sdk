from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_budget_status_result import GetBudgetStatusResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cost_center: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["costCenter"] = cost_center

    params["date"] = date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/budget-control/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetBudgetStatusResult]:
    if response.status_code == 200:
        response_200 = GetBudgetStatusResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetBudgetStatusResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cost_center: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
) -> Response[GetBudgetStatusResult]:
    """[Buyer] Budget, committed (approved orders not yet invoiced), actual (approved invoices) and
    remaining per cost center for the current period

    Args:
        cost_center (Union[Unset, str]):
        date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetStatusResult]
    """

    kwargs = _get_kwargs(
        cost_center=cost_center,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cost_center: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
) -> Optional[GetBudgetStatusResult]:
    """[Buyer] Budget, committed (approved orders not yet invoiced), actual (approved invoices) and
    remaining per cost center for the current period

    Args:
        cost_center (Union[Unset, str]):
        date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetStatusResult
    """

    return sync_detailed(
        client=client,
        cost_center=cost_center,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cost_center: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
) -> Response[GetBudgetStatusResult]:
    """[Buyer] Budget, committed (approved orders not yet invoiced), actual (approved invoices) and
    remaining per cost center for the current period

    Args:
        cost_center (Union[Unset, str]):
        date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBudgetStatusResult]
    """

    kwargs = _get_kwargs(
        cost_center=cost_center,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cost_center: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
) -> Optional[GetBudgetStatusResult]:
    """[Buyer] Budget, committed (approved orders not yet invoiced), actual (approved invoices) and
    remaining per cost center for the current period

    Args:
        cost_center (Union[Unset, str]):
        date (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBudgetStatusResult
    """

    return (
        await asyncio_detailed(
            client=client,
            cost_center=cost_center,
            date=date,
        )
    ).parsed
