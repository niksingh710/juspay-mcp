import httpx
from juspay_tools.config import ENDPOINTS
from juspay_tools.api.utils import post

async def session_api_juspay(payload: dict) -> dict:
    """
    Creates a Juspay payment session to initiate a transaction.

    This function sends an HTTP POST request (JSON body) to the Juspay Session endpoint.
    It includes payment details like order_id, amount, customer info, and return URL.
    If 'customer_id' is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): A dictionary representing the JSON body for the session request.
                        Must contain required fields specified in the juspay_session_schema
                        (e.g., order_id, amount, customer_id, customer_email, etc.).

    Returns:
        dict: Parsed JSON response from the Juspay Session API. This typically contains
              details needed to launch the payment page or SDK.

    Raises:
        Exception: If the API call fails (e.g., HTTP error, network issue, invalid input).
    """
    api_url = ENDPOINTS["session"]
    await post(api_url, payload)
