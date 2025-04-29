import logging

from juspay_dashboard_mcp.api.utils import post, call, get_juspay_host_from_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def get_offer_details_juspay(payload: dict) -> dict:
    """
    Retrieves detailed information for a specific offer.

    The API endpoint is:
        https://portal.juspay.in/api/offers/dashboard/uploads/{offerId}

    The call uses URL parameters:
        - is_batch: Whether it's a batch offer (true/false)
        - merchant_id: Optional merchant ID for the offer

    Headers include:
        - x-tenant-id from payload
        - x-web-logintoken from payload
        - content-type: application/json

    Args:
        payload (dict): A dictionary with the following required key:
            - offerId: The unique offer ID to retrieve details for.
        May include:
            - merchantId: Optional merchant ID for the offer.
            - isBatch: Optional boolean to indicate if it's a batch offer (default: False).

    Returns:
        dict: The parsed JSON response containing offer details.

    Raises:
        ValueError: If offerId is missing.
        Exception: If the API call fails.
    """
    offer_id = payload.get("offerId")
    if not offer_id:
        raise ValueError("'offerId' is required in the payload")

    merchant_id = payload.get("merchantId", "")
    is_batch = "true" if payload.get("isBatch", False) else "false"

    host = await get_juspay_host_from_api(token=payload.get("web_login_str"))
    api_url = f"{host}api/offers/dashboard/uploads/{offer_id}?is_batch={is_batch}"
    
    if merchant_id:
        api_url += f"&merchant_id={merchant_id}"
    
    return await call(api_url, payload)

async def list_offers_juspay(payload: dict) -> dict:
    """
    Lists all offers configured by the merchant, along with key details such as 
    status, PMT, offer code, start/end times, and benefit types.

    The API endpoint is:
        https://portal.juspay.in/api/offers/dashboard/dashboard-list

    The call uses URL parameters:
        - merchant_id: Merchant identifier

    And JSON body containing:
        - merchant_id: Merchant identifier
        - start_time: Start time for filtering offers
        - end_time: End time for filtering offers

    Headers include:
        - x-tenant-id from payload
        - x-web-logintoken from payload
        - content-type: application/json

    Args:
        payload (dict): A dictionary containing:
            - merchant_id: Merchant identifier.
            - start_time: Start time for filtering offers.
            - end_time: End time for filtering offers.

    Returns:
        dict: The parsed JSON response from the Juspay List Offers API.

    Raises:
        ValueError: If required parameters are missing.
        Exception: If the API call fails.
    """
    if "merchant_id" not in payload or "start_time" not in payload or "end_time" not in payload:
        raise ValueError("Payload must contain 'merchant_id', 'start_time', and 'end_time'.")

    merchant_id = payload.get("merchant_id")
    host = await get_juspay_host_from_api(token=payload.get("web_login_str"))
    api_url = f"{host}api/offers/dashboard/dashboard-list?merchant_id={merchant_id}"
    
    return await post(api_url, payload)