from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.focus_destination_view import FocusDestinationView
from ...models.put_focus_destination_input import PutFocusDestinationInput
from ...types import Response


def _get_kwargs(
    *,
    body: PutFocusDestinationInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/focus-destination",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FocusDestinationView]:
    if response.status_code == 200:
        response_200 = FocusDestinationView.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FocusDestinationView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFocusDestinationInput,
) -> Response[FocusDestinationView]:
    """[Buyer] Set where Pleaxy delivers FOCUS files: bucket, folder (prefix), region, format (csv,
    gzipped, or parquet), FOCUS version (1.2 or 1.4) and include (all or non_cloud). Without roleArn it
    saves the destination awaiting its PleaxyFocusWriter role and returns the External ID for the stack;
    with roleArn Pleaxy writes and deletes a test object first and saves nothing if it can't. Every day
    Pleaxy then writes this month (and, through the 5th, last month) as one file per month under
    <prefix>/focus/<version>/billing_period=YYYY-MM/. 'edit' on invoices; a signed-in person only.

    Args:
        body (PutFocusDestinationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FocusDestinationView]
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
    body: PutFocusDestinationInput,
) -> Optional[FocusDestinationView]:
    """[Buyer] Set where Pleaxy delivers FOCUS files: bucket, folder (prefix), region, format (csv,
    gzipped, or parquet), FOCUS version (1.2 or 1.4) and include (all or non_cloud). Without roleArn it
    saves the destination awaiting its PleaxyFocusWriter role and returns the External ID for the stack;
    with roleArn Pleaxy writes and deletes a test object first and saves nothing if it can't. Every day
    Pleaxy then writes this month (and, through the 5th, last month) as one file per month under
    <prefix>/focus/<version>/billing_period=YYYY-MM/. 'edit' on invoices; a signed-in person only.

    Args:
        body (PutFocusDestinationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FocusDestinationView
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFocusDestinationInput,
) -> Response[FocusDestinationView]:
    """[Buyer] Set where Pleaxy delivers FOCUS files: bucket, folder (prefix), region, format (csv,
    gzipped, or parquet), FOCUS version (1.2 or 1.4) and include (all or non_cloud). Without roleArn it
    saves the destination awaiting its PleaxyFocusWriter role and returns the External ID for the stack;
    with roleArn Pleaxy writes and deletes a test object first and saves nothing if it can't. Every day
    Pleaxy then writes this month (and, through the 5th, last month) as one file per month under
    <prefix>/focus/<version>/billing_period=YYYY-MM/. 'edit' on invoices; a signed-in person only.

    Args:
        body (PutFocusDestinationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FocusDestinationView]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutFocusDestinationInput,
) -> Optional[FocusDestinationView]:
    """[Buyer] Set where Pleaxy delivers FOCUS files: bucket, folder (prefix), region, format (csv,
    gzipped, or parquet), FOCUS version (1.2 or 1.4) and include (all or non_cloud). Without roleArn it
    saves the destination awaiting its PleaxyFocusWriter role and returns the External ID for the stack;
    with roleArn Pleaxy writes and deletes a test object first and saves nothing if it can't. Every day
    Pleaxy then writes this month (and, through the 5th, last month) as one file per month under
    <prefix>/focus/<version>/billing_period=YYYY-MM/. 'edit' on invoices; a signed-in person only.

    Args:
        body (PutFocusDestinationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FocusDestinationView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
