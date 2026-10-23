from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.budget_control_settings import BudgetControlSettings
from ...models.update_budget_control_input import UpdateBudgetControlInput
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateBudgetControlInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/budget-control",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BudgetControlSettings]:
    if response.status_code == 200:
        response_200 = BudgetControlSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BudgetControlSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateBudgetControlInput,
) -> Response[BudgetControlSettings]:
    """[Buyer] Change budget control. Applies to orders and requests submitted or approved from now on.
    Needs a signed-in session.

    Args:
        body (UpdateBudgetControlInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetControlSettings]
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
    body: UpdateBudgetControlInput,
) -> Optional[BudgetControlSettings]:
    """[Buyer] Change budget control. Applies to orders and requests submitted or approved from now on.
    Needs a signed-in session.

    Args:
        body (UpdateBudgetControlInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetControlSettings
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateBudgetControlInput,
) -> Response[BudgetControlSettings]:
    """[Buyer] Change budget control. Applies to orders and requests submitted or approved from now on.
    Needs a signed-in session.

    Args:
        body (UpdateBudgetControlInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BudgetControlSettings]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateBudgetControlInput,
) -> Optional[BudgetControlSettings]:
    """[Buyer] Change budget control. Applies to orders and requests submitted or approved from now on.
    Needs a signed-in session.

    Args:
        body (UpdateBudgetControlInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BudgetControlSettings
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
