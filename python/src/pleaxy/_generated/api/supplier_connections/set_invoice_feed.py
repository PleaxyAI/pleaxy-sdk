from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_invoice_feed_input import SetInvoiceFeedInput
from ...models.set_invoice_feed_result_type_0 import SetInvoiceFeedResultType0
from ...models.set_invoice_feed_result_type_1 import SetInvoiceFeedResultType1
from ...types import Response


def _get_kwargs(
    connection_id: str,
    *,
    body: SetInvoiceFeedInput,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/supplier-connections/{connection_id}/invoice-feed".format(
            connection_id=connection_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_set_invoice_feed_result_type_0 = (
                    SetInvoiceFeedResultType0.from_dict(data)
                )

                return componentsschemas_set_invoice_feed_result_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_set_invoice_feed_result_type_1 = (
                SetInvoiceFeedResultType1.from_dict(data)
            )

            return componentsschemas_set_invoice_feed_result_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
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
    body: SetInvoiceFeedInput,
) -> Response[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
    """[Buyer] Turn this supplier's automated invoices on or off - whether it may send invoices to you with
    an invoices:feed API key (POST .../invoices/connections/:connectionId). On from the moment you
    approve the supplier; turning it off refuses the very next one, and invoices already received stay.
    Approved connections only (400 COUNTERPARTY_NOT_ACTIVE). Human session only.

    Args:
        connection_id (str):
        body (SetInvoiceFeedInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SetInvoiceFeedResultType0', 'SetInvoiceFeedResultType1']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetInvoiceFeedInput,
) -> Optional[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
    """[Buyer] Turn this supplier's automated invoices on or off - whether it may send invoices to you with
    an invoices:feed API key (POST .../invoices/connections/:connectionId). On from the moment you
    approve the supplier; turning it off refuses the very next one, and invoices already received stay.
    Approved connections only (400 COUNTERPARTY_NOT_ACTIVE). Human session only.

    Args:
        connection_id (str):
        body (SetInvoiceFeedInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SetInvoiceFeedResultType0', 'SetInvoiceFeedResultType1']
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetInvoiceFeedInput,
) -> Response[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
    """[Buyer] Turn this supplier's automated invoices on or off - whether it may send invoices to you with
    an invoices:feed API key (POST .../invoices/connections/:connectionId). On from the moment you
    approve the supplier; turning it off refuses the very next one, and invoices already received stay.
    Approved connections only (400 COUNTERPARTY_NOT_ACTIVE). Human session only.

    Args:
        connection_id (str):
        body (SetInvoiceFeedInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SetInvoiceFeedResultType0', 'SetInvoiceFeedResultType1']]
    """

    kwargs = _get_kwargs(
        connection_id=connection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetInvoiceFeedInput,
) -> Optional[Union["SetInvoiceFeedResultType0", "SetInvoiceFeedResultType1"]]:
    """[Buyer] Turn this supplier's automated invoices on or off - whether it may send invoices to you with
    an invoices:feed API key (POST .../invoices/connections/:connectionId). On from the moment you
    approve the supplier; turning it off refuses the very next one, and invoices already received stay.
    Approved connections only (400 COUNTERPARTY_NOT_ACTIVE). Human session only.

    Args:
        connection_id (str):
        body (SetInvoiceFeedInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SetInvoiceFeedResultType0', 'SetInvoiceFeedResultType1']
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            body=body,
        )
    ).parsed
