from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.supplier_directory_page import SupplierDirectoryPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, str] = UNSET,
    segment: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["offset"] = offset

    params["segment"] = segment

    params["category"] = category

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/supplier-connections/directory/browse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SupplierDirectoryPage]:
    if response.status_code == 200:
        response_200 = SupplierDirectoryPage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SupplierDirectoryPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, str] = UNSET,
    segment: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[SupplierDirectoryPage]:
    """[Buyer] Browse the suppliers that chose to be found on Pleaxy, to find one you don't work with yet:
    all of them, or by `category` (a Pleaxy category id such as `software`), by `segment` (a two-digit
    UN standard code such as `43`; a category's suppliers are found under its segments too) and by `q`,
    part of a name. Each has its listed regions with the `directoryId` it is invited by in Pleaxy, what
    it says it sells, `verified` when Pleaxy confirmed who it is, `sponsored` when it pays to be shown
    first, and `connectionId` when it is already one of your suppliers. Up to 3 sponsored suppliers that
    match come first, then A to Z; 60 companies a page, the next from `nextOffset`; `total` counts every
    match. Never a contact email. Everything a supplier lists is its own claim unless `verified`

    Args:
        offset (Union[Unset, str]):
        segment (Union[Unset, str]):
        category (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupplierDirectoryPage]
    """

    kwargs = _get_kwargs(
        offset=offset,
        segment=segment,
        category=category,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, str] = UNSET,
    segment: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[SupplierDirectoryPage]:
    """[Buyer] Browse the suppliers that chose to be found on Pleaxy, to find one you don't work with yet:
    all of them, or by `category` (a Pleaxy category id such as `software`), by `segment` (a two-digit
    UN standard code such as `43`; a category's suppliers are found under its segments too) and by `q`,
    part of a name. Each has its listed regions with the `directoryId` it is invited by in Pleaxy, what
    it says it sells, `verified` when Pleaxy confirmed who it is, `sponsored` when it pays to be shown
    first, and `connectionId` when it is already one of your suppliers. Up to 3 sponsored suppliers that
    match come first, then A to Z; 60 companies a page, the next from `nextOffset`; `total` counts every
    match. Never a contact email. Everything a supplier lists is its own claim unless `verified`

    Args:
        offset (Union[Unset, str]):
        segment (Union[Unset, str]):
        category (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupplierDirectoryPage
    """

    return sync_detailed(
        client=client,
        offset=offset,
        segment=segment,
        category=category,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, str] = UNSET,
    segment: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[SupplierDirectoryPage]:
    """[Buyer] Browse the suppliers that chose to be found on Pleaxy, to find one you don't work with yet:
    all of them, or by `category` (a Pleaxy category id such as `software`), by `segment` (a two-digit
    UN standard code such as `43`; a category's suppliers are found under its segments too) and by `q`,
    part of a name. Each has its listed regions with the `directoryId` it is invited by in Pleaxy, what
    it says it sells, `verified` when Pleaxy confirmed who it is, `sponsored` when it pays to be shown
    first, and `connectionId` when it is already one of your suppliers. Up to 3 sponsored suppliers that
    match come first, then A to Z; 60 companies a page, the next from `nextOffset`; `total` counts every
    match. Never a contact email. Everything a supplier lists is its own claim unless `verified`

    Args:
        offset (Union[Unset, str]):
        segment (Union[Unset, str]):
        category (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupplierDirectoryPage]
    """

    kwargs = _get_kwargs(
        offset=offset,
        segment=segment,
        category=category,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, str] = UNSET,
    segment: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[SupplierDirectoryPage]:
    """[Buyer] Browse the suppliers that chose to be found on Pleaxy, to find one you don't work with yet:
    all of them, or by `category` (a Pleaxy category id such as `software`), by `segment` (a two-digit
    UN standard code such as `43`; a category's suppliers are found under its segments too) and by `q`,
    part of a name. Each has its listed regions with the `directoryId` it is invited by in Pleaxy, what
    it says it sells, `verified` when Pleaxy confirmed who it is, `sponsored` when it pays to be shown
    first, and `connectionId` when it is already one of your suppliers. Up to 3 sponsored suppliers that
    match come first, then A to Z; 60 companies a page, the next from `nextOffset`; `total` counts every
    match. Never a contact email. Everything a supplier lists is its own claim unless `verified`

    Args:
        offset (Union[Unset, str]):
        segment (Union[Unset, str]):
        category (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupplierDirectoryPage
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            segment=segment,
            category=category,
            q=q,
        )
    ).parsed
