from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_reference_rate_result import GetReferenceRateResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["date"] = date

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/reference-rate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetReferenceRateResult]:
    if response.status_code == 200:
        response_200 = GetReferenceRateResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetReferenceRateResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[GetReferenceRateResult]:
    """[Buyer, Supplier] The reference rate for 1 `from` in `to` on `date` (YYYY-MM-DD, default today), or
    the latest of the 3 days before it. Returns `{ reference }`, absent when there's no rate. A
    suggestion for the New invoice form only; the invoice records whatever rate is submitted. Signed-in
    session only. Rates By Exchange Rate API.

    Args:
        date (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReferenceRateResult]
    """

    kwargs = _get_kwargs(
        date=date,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[GetReferenceRateResult]:
    """[Buyer, Supplier] The reference rate for 1 `from` in `to` on `date` (YYYY-MM-DD, default today), or
    the latest of the 3 days before it. Returns `{ reference }`, absent when there's no rate. A
    suggestion for the New invoice form only; the invoice records whatever rate is submitted. Signed-in
    session only. Rates By Exchange Rate API.

    Args:
        date (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReferenceRateResult
    """

    return sync_detailed(
        client=client,
        date=date,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[GetReferenceRateResult]:
    """[Buyer, Supplier] The reference rate for 1 `from` in `to` on `date` (YYYY-MM-DD, default today), or
    the latest of the 3 days before it. Returns `{ reference }`, absent when there's no rate. A
    suggestion for the New invoice form only; the invoice records whatever rate is submitted. Signed-in
    session only. Rates By Exchange Rate API.

    Args:
        date (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetReferenceRateResult]
    """

    kwargs = _get_kwargs(
        date=date,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[GetReferenceRateResult]:
    """[Buyer, Supplier] The reference rate for 1 `from` in `to` on `date` (YYYY-MM-DD, default today), or
    the latest of the 3 days before it. Returns `{ reference }`, absent when there's no rate. A
    suggestion for the New invoice form only; the invoice records whatever rate is submitted. Signed-in
    session only. Rates By Exchange Rate API.

    Args:
        date (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetReferenceRateResult
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            from_=from_,
            to=to,
        )
    ).parsed
