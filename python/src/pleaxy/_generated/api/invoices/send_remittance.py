from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.invoice_buyer_view import InvoiceBuyerView
from ...models.send_remittance_input import SendRemittanceInput
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    body: SendRemittanceInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/invoices/{invoice_id}/remittance".format(
            invoice_id=invoice_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InvoiceBuyerView]:
    if response.status_code == 201:
        response_201 = InvoiceBuyerView.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InvoiceBuyerView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SendRemittanceInput,
) -> Response[InvoiceBuyerView]:
    """[Buyer] Send the supplier a remittance for a paid invoice: { note?, file?: { fileId, fileName } },
    at least one. The note (up to 1,000 characters) goes in the supplier's notification, which its Slack
    or Teams channel also gets when routed there; the file is a proof of payment uploaded with
    RequestRemittanceUpload. Up to 20 per invoice. 409 REMITTANCE_NEEDS_PAYMENT before a payment is
    recorded. Human session only.

    Args:
        invoice_id (str):
        body (SendRemittanceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceBuyerView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SendRemittanceInput,
) -> Optional[InvoiceBuyerView]:
    """[Buyer] Send the supplier a remittance for a paid invoice: { note?, file?: { fileId, fileName } },
    at least one. The note (up to 1,000 characters) goes in the supplier's notification, which its Slack
    or Teams channel also gets when routed there; the file is a proof of payment uploaded with
    RequestRemittanceUpload. Up to 20 per invoice. 409 REMITTANCE_NEEDS_PAYMENT before a payment is
    recorded. Human session only.

    Args:
        invoice_id (str):
        body (SendRemittanceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceBuyerView
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SendRemittanceInput,
) -> Response[InvoiceBuyerView]:
    """[Buyer] Send the supplier a remittance for a paid invoice: { note?, file?: { fileId, fileName } },
    at least one. The note (up to 1,000 characters) goes in the supplier's notification, which its Slack
    or Teams channel also gets when routed there; the file is a proof of payment uploaded with
    RequestRemittanceUpload. Up to 20 per invoice. 409 REMITTANCE_NEEDS_PAYMENT before a payment is
    recorded. Human session only.

    Args:
        invoice_id (str):
        body (SendRemittanceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvoiceBuyerView]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SendRemittanceInput,
) -> Optional[InvoiceBuyerView]:
    """[Buyer] Send the supplier a remittance for a paid invoice: { note?, file?: { fileId, fileName } },
    at least one. The note (up to 1,000 characters) goes in the supplier's notification, which its Slack
    or Teams channel also gets when routed there; the file is a proof of payment uploaded with
    RequestRemittanceUpload. Up to 20 per invoice. 409 REMITTANCE_NEEDS_PAYMENT before a payment is
    recorded. Human session only.

    Args:
        invoice_id (str):
        body (SendRemittanceInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvoiceBuyerView
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
