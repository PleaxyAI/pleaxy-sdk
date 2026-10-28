from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.supplier_risk import SupplierRisk
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/supplier-risk",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["SupplierRisk"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SupplierRisk.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["SupplierRisk"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["SupplierRisk"]]:
    """[Buyer] Each supplier's risk: level ok|attention|blocked (blocked = a confirmed sanctions match;
    never a score), and its rows - bank (accounts waiting for approval), screening (status),
    flaggedAnswers (count) and missingDocuments (the questions' labels), each with a state
    ok|attention|blocked|none. A screening that isn't flagged shows as none here; read one supplier for
    its full screening and bank status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['SupplierRisk']]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["SupplierRisk"]]:
    """[Buyer] Each supplier's risk: level ok|attention|blocked (blocked = a confirmed sanctions match;
    never a score), and its rows - bank (accounts waiting for approval), screening (status),
    flaggedAnswers (count) and missingDocuments (the questions' labels), each with a state
    ok|attention|blocked|none. A screening that isn't flagged shows as none here; read one supplier for
    its full screening and bank status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['SupplierRisk']
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["SupplierRisk"]]:
    """[Buyer] Each supplier's risk: level ok|attention|blocked (blocked = a confirmed sanctions match;
    never a score), and its rows - bank (accounts waiting for approval), screening (status),
    flaggedAnswers (count) and missingDocuments (the questions' labels), each with a state
    ok|attention|blocked|none. A screening that isn't flagged shows as none here; read one supplier for
    its full screening and bank status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['SupplierRisk']]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["SupplierRisk"]]:
    """[Buyer] Each supplier's risk: level ok|attention|blocked (blocked = a confirmed sanctions match;
    never a score), and its rows - bank (accounts waiting for approval), screening (status),
    flaggedAnswers (count) and missingDocuments (the questions' labels), each with a state
    ok|attention|blocked|none. A screening that isn't flagged shows as none here; read one supplier for
    its full screening and bank status.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['SupplierRisk']
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
