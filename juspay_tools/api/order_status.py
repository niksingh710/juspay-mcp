import httpx
from juspay_tools.config import ENDPOINTS 
from juspay_tools.api.utils import call

async def order_status_api_juspay(payload: dict) -> dict:
    """
    Retrieves the status of a specific Juspay order using the order_id.

    This function sends an HTTP GET request to the Juspay Order Status endpoint.
    The 'order_id' from the payload is appended to the URL. If 'customer_id'
    is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): Must include:
            - order_id (str): Unique identifier of the order to check.
        May include:
            - customer_id (str, optional): If provided, used for the x-routing-id header.

    Returns:
        dict: Parsed JSON response from the Juspay Order Status API, containing details
              about the order, such as its status.

    Raises:
        ValueError: If 'order_id' is missing in the payload.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")

    customer_id = payload.get("customer_id")

    api_url = ENDPOINTS["order_status"].format(order_id=order_id)
    await call(api_url, customer_id)
