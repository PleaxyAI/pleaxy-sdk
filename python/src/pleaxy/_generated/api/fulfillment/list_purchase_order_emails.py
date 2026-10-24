from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_order_emails import PurchaseOrderEmails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    po_id: str,
    *,
    buyer: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["buyer"] = buyer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/purchase-orders/{po_id}/emails".format(
            po_id=po_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PurchaseOrderEmails]:
    if response.status_code == 200:
        response_200 = PurchaseOrderEmails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PurchaseOrderEmails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderEmails]:
    """[Both] The order's own email address and the emails that reached it, newest first: { address?,
    emails: [{ id, from, subject, receivedAt, trust: verified|unverified, kind: cxml|text, outcome:
    applied|draft|held|noAction|test|failed|ignored, reasonCode?, reason?, summary?, text?, attachments,
    draft?, result?, decision? }] }. A supplier replying to the order email, or its system sending a
    cXML ConfirmationRequest or ShipNoticeRequest, reaches this address. A verified sender's cXML
    document is recorded at once (applied); a plain email is read by the Pleaxy Assistant into a draft
    confirmation or ship notice, and an unverified sender's cXML document is held, both for someone to
    record with RecordPurchaseOrderEmail. address is absent until the order is issued, or when email-in
    is off. Takes the same ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderEmails]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderEmails]:
    """[Both] The order's own email address and the emails that reached it, newest first: { address?,
    emails: [{ id, from, subject, receivedAt, trust: verified|unverified, kind: cxml|text, outcome:
    applied|draft|held|noAction|test|failed|ignored, reasonCode?, reason?, summary?, text?, attachments,
    draft?, result?, decision? }] }. A supplier replying to the order email, or its system sending a
    cXML ConfirmationRequest or ShipNoticeRequest, reaches this address. A verified sender's cXML
    document is recorded at once (applied); a plain email is read by the Pleaxy Assistant into a draft
    confirmation or ship notice, and an unverified sender's cXML document is held, both for someone to
    record with RecordPurchaseOrderEmail. address is absent until the order is issued, or when email-in
    is off. Takes the same ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderEmails
    """

    return sync_detailed(
        po_id=po_id,
        client=client,
        buyer=buyer,
    ).parsed


async def asyncio_detailed(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Response[PurchaseOrderEmails]:
    """[Both] The order's own email address and the emails that reached it, newest first: { address?,
    emails: [{ id, from, subject, receivedAt, trust: verified|unverified, kind: cxml|text, outcome:
    applied|draft|held|noAction|test|failed|ignored, reasonCode?, reason?, summary?, text?, attachments,
    draft?, result?, decision? }] }. A supplier replying to the order email, or its system sending a
    cXML ConfirmationRequest or ShipNoticeRequest, reaches this address. A verified sender's cXML
    document is recorded at once (applied); a plain email is read by the Pleaxy Assistant into a draft
    confirmation or ship notice, and an unverified sender's cXML document is held, both for someone to
    record with RecordPurchaseOrderEmail. address is absent until the order is issued, or when email-in
    is off. Takes the same ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseOrderEmails]
    """

    kwargs = _get_kwargs(
        po_id=po_id,
        buyer=buyer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    po_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    buyer: Union[Unset, str] = UNSET,
) -> Optional[PurchaseOrderEmails]:
    """[Both] The order's own email address and the emails that reached it, newest first: { address?,
    emails: [{ id, from, subject, receivedAt, trust: verified|unverified, kind: cxml|text, outcome:
    applied|draft|held|noAction|test|failed|ignored, reasonCode?, reason?, summary?, text?, attachments,
    draft?, result?, decision? }] }. A supplier replying to the order email, or its system sending a
    cXML ConfirmationRequest or ShipNoticeRequest, reaches this address. A verified sender's cXML
    document is recorded at once (applied); a plain email is read by the Pleaxy Assistant into a draft
    confirmation or ship notice, and an unverified sender's cXML document is held, both for someone to
    record with RecordPurchaseOrderEmail. address is absent until the order is issued, or when email-in
    is off. Takes the same ?buyer= as GetPurchaseOrder.

    Args:
        po_id (str):
        buyer (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseOrderEmails
    """

    return (
        await asyncio_detailed(
            po_id=po_id,
            client=client,
            buyer=buyer,
        )
    ).parsed
