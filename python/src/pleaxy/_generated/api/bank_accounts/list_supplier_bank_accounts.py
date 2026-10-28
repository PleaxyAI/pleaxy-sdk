from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bank_account_view import BankAccountView
from ...types import Response


def _get_kwargs(
    connection_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/bank-accounts/suppliers/{connection_id}".format(
            connection_id=connection_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["BankAccountView"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BankAccountView.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["BankAccountView"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["BankAccountView"]]:
    """[Buyer] A supplier's bank accounts on file, one per billing lane (payee and currency): details
    masked to the last four, status unverified|verified|changing, how each was approved
    (approval.verification: supplier_confirmed|buyer_approved|paid_before, approval.check.method) and
    the last 10 events.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BankAccountView']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["BankAccountView"]]:
    """[Buyer] A supplier's bank accounts on file, one per billing lane (payee and currency): details
    masked to the last four, status unverified|verified|changing, how each was approved
    (approval.verification: supplier_confirmed|buyer_approved|paid_before, approval.check.method) and
    the last 10 events.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BankAccountView']
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["BankAccountView"]]:
    """[Buyer] A supplier's bank accounts on file, one per billing lane (payee and currency): details
    masked to the last four, status unverified|verified|changing, how each was approved
    (approval.verification: supplier_confirmed|buyer_approved|paid_before, approval.check.method) and
    the last 10 events.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BankAccountView']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["BankAccountView"]]:
    """[Buyer] A supplier's bank accounts on file, one per billing lane (payee and currency): details
    masked to the last four, status unverified|verified|changing, how each was approved
    (approval.verification: supplier_confirmed|buyer_approved|paid_before, approval.check.method) and
    the last 10 events.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['BankAccountView']
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
