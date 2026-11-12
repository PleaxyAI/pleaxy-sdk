from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sourcing_comparison import SourcingComparison
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rfq_id: str,
    *,
    round_: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["round"] = round_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sourcing-events/{rfq_id}/comparison".format(
            rfq_id=rfq_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SourcingComparison]:
    if response.status_code == 200:
        response_200 = SourcingComparison.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SourcingComparison]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    round_: Union[Unset, float] = UNSET,
) -> Response[SourcingComparison]:
    """[Buyer] The answers side by side: per line each price and total (lowest marked), totals, lead times
    against needed-by, terms, risk and onboarding; with criteria the weighted total, with evaluators
    their averages and spread (hidden from an evaluator until its own scorecard is in). `?round=n` shows
    an earlier round (default the latest). Refused while the current round is sealed

    Args:
        rfq_id (str):
        round_ (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SourcingComparison]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
        round_=round_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    round_: Union[Unset, float] = UNSET,
) -> Optional[SourcingComparison]:
    """[Buyer] The answers side by side: per line each price and total (lowest marked), totals, lead times
    against needed-by, terms, risk and onboarding; with criteria the weighted total, with evaluators
    their averages and spread (hidden from an evaluator until its own scorecard is in). `?round=n` shows
    an earlier round (default the latest). Refused while the current round is sealed

    Args:
        rfq_id (str):
        round_ (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SourcingComparison
    """

    return sync_detailed(
        rfq_id=rfq_id,
        client=client,
        round_=round_,
    ).parsed


async def asyncio_detailed(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    round_: Union[Unset, float] = UNSET,
) -> Response[SourcingComparison]:
    """[Buyer] The answers side by side: per line each price and total (lowest marked), totals, lead times
    against needed-by, terms, risk and onboarding; with criteria the weighted total, with evaluators
    their averages and spread (hidden from an evaluator until its own scorecard is in). `?round=n` shows
    an earlier round (default the latest). Refused while the current round is sealed

    Args:
        rfq_id (str):
        round_ (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SourcingComparison]
    """

    kwargs = _get_kwargs(
        rfq_id=rfq_id,
        round_=round_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rfq_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    round_: Union[Unset, float] = UNSET,
) -> Optional[SourcingComparison]:
    """[Buyer] The answers side by side: per line each price and total (lowest marked), totals, lead times
    against needed-by, terms, risk and onboarding; with criteria the weighted total, with evaluators
    their averages and spread (hidden from an evaluator until its own scorecard is in). `?round=n` shows
    an earlier round (default the latest). Refused while the current round is sealed

    Args:
        rfq_id (str):
        round_ (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SourcingComparison
    """

    return (
        await asyncio_detailed(
            rfq_id=rfq_id,
            client=client,
            round_=round_,
        )
    ).parsed
