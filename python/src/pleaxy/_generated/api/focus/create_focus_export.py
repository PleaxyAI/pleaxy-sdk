from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_focus_export_input import CreateFocusExportInput
from ...models.focus_export import FocusExport
from ...types import Response


def _get_kwargs(
    *,
    body: CreateFocusExportInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/focus-exports",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FocusExport]:
    if response.status_code == 201:
        response_201 = FocusExport.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FocusExport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusExportInput,
) -> Response[FocusExport]:
    """[Buyer] Export the workspace's invoices, debit notes and accepted credit notes for billing periods
    from..to (YYYY-MM, at most 36 months) as a FOCUS Cost and Usage dataset in CSV (version 1.2 by
    default, or 1.4), with a metadata file. One row per line, tax entry and adjustment; credit notes
    negative; amounts in each document's currency. include=non_cloud leaves out cloud and AI providers'
    invoices. Returns download links valid 15 minutes; the files are kept 7 days. 'view' on invoices.

    Args:
        body (CreateFocusExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FocusExport]
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
    body: CreateFocusExportInput,
) -> Optional[FocusExport]:
    """[Buyer] Export the workspace's invoices, debit notes and accepted credit notes for billing periods
    from..to (YYYY-MM, at most 36 months) as a FOCUS Cost and Usage dataset in CSV (version 1.2 by
    default, or 1.4), with a metadata file. One row per line, tax entry and adjustment; credit notes
    negative; amounts in each document's currency. include=non_cloud leaves out cloud and AI providers'
    invoices. Returns download links valid 15 minutes; the files are kept 7 days. 'view' on invoices.

    Args:
        body (CreateFocusExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FocusExport
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusExportInput,
) -> Response[FocusExport]:
    """[Buyer] Export the workspace's invoices, debit notes and accepted credit notes for billing periods
    from..to (YYYY-MM, at most 36 months) as a FOCUS Cost and Usage dataset in CSV (version 1.2 by
    default, or 1.4), with a metadata file. One row per line, tax entry and adjustment; credit notes
    negative; amounts in each document's currency. include=non_cloud leaves out cloud and AI providers'
    invoices. Returns download links valid 15 minutes; the files are kept 7 days. 'view' on invoices.

    Args:
        body (CreateFocusExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FocusExport]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateFocusExportInput,
) -> Optional[FocusExport]:
    """[Buyer] Export the workspace's invoices, debit notes and accepted credit notes for billing periods
    from..to (YYYY-MM, at most 36 months) as a FOCUS Cost and Usage dataset in CSV (version 1.2 by
    default, or 1.4), with a metadata file. One row per line, tax entry and adjustment; credit notes
    negative; amounts in each document's currency. include=non_cloud leaves out cloud and AI providers'
    invoices. Returns download links valid 15 minutes; the files are kept 7 days. 'view' on invoices.

    Args:
        body (CreateFocusExportInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FocusExport
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
