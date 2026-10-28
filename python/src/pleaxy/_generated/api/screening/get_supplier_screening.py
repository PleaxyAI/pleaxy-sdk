from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_supplier_screening_result import GetSupplierScreeningResult
from ...types import Response


def _get_kwargs(
    connection_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/screening/suppliers/{connection_id}".format(
            connection_id=connection_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetSupplierScreeningResult]:
    if response.status_code == 200:
        response_200 = GetSupplierScreeningResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetSupplierScreeningResult]:
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
) -> Response[GetSupplierScreeningResult]:
    """[Buyer] A supplier's sanctions screening: { enabled, screening? } with status
    clear|possible_match|confirmed_match, the names screened (subjects: its name, an earlier name, its
    bank accounts' payees), the list versions, and matches - each the listed entry it resembles (list,
    names, countries, programmes), the score, and its state open|dismissed|confirmed|closed with who
    decided and why.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSupplierScreeningResult]
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
) -> Optional[GetSupplierScreeningResult]:
    """[Buyer] A supplier's sanctions screening: { enabled, screening? } with status
    clear|possible_match|confirmed_match, the names screened (subjects: its name, an earlier name, its
    bank accounts' payees), the list versions, and matches - each the listed entry it resembles (list,
    names, countries, programmes), the score, and its state open|dismissed|confirmed|closed with who
    decided and why.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSupplierScreeningResult
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetSupplierScreeningResult]:
    """[Buyer] A supplier's sanctions screening: { enabled, screening? } with status
    clear|possible_match|confirmed_match, the names screened (subjects: its name, an earlier name, its
    bank accounts' payees), the list versions, and matches - each the listed entry it resembles (list,
    names, countries, programmes), the score, and its state open|dismissed|confirmed|closed with who
    decided and why.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSupplierScreeningResult]
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
) -> Optional[GetSupplierScreeningResult]:
    """[Buyer] A supplier's sanctions screening: { enabled, screening? } with status
    clear|possible_match|confirmed_match, the names screened (subjects: its name, an earlier name, its
    bank accounts' payees), the list versions, and matches - each the listed entry it resembles (list,
    names, countries, programmes), the score, and its state open|dismissed|confirmed|closed with who
    decided and why.

    Args:
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSupplierScreeningResult
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
        )
    ).parsed
