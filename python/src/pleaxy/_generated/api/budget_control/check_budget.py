from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_check import BudgetCheck
from ...models.budget_check_input import BudgetCheckInput
from ...types import Response


def _get_kwargs(
    *,
    body: BudgetCheckInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/budget-control/check",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BudgetCheck]:
    if response.status_code == 200:
        response_200 = BudgetCheck.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BudgetCheck]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BudgetCheckInput,
) -> Response[BudgetCheck]:
    """[Buyer] Preview the budget check for an amount on a cost center: within, over, no_budget, no_rate or
    off. Writes nothing.

    Args:
        body (BudgetCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetCheck]
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
    body: BudgetCheckInput,
) -> Optional[BudgetCheck]:
    """[Buyer] Preview the budget check for an amount on a cost center: within, over, no_budget, no_rate or
    off. Writes nothing.

    Args:
        body (BudgetCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetCheck
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BudgetCheckInput,
) -> Response[BudgetCheck]:
    """[Buyer] Preview the budget check for an amount on a cost center: within, over, no_budget, no_rate or
    off. Writes nothing.

    Args:
        body (BudgetCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetCheck]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: BudgetCheckInput,
) -> Optional[BudgetCheck]:
    """[Buyer] Preview the budget check for an amount on a cost center: within, over, no_budget, no_rate or
    off. Writes nothing.

    Args:
        body (BudgetCheckInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetCheck
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
