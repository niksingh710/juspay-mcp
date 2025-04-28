import httpx
from juspay_tools.config import ENDPOINTS 
from juspay_tools.api.utils import call

async def get_customer_juspay(payload: dict) -> dict:
    """
    Retrieves customer details from Juspay using the customer_id.

    This function sends an HTTP GET request to the Juspay Get Customer endpoint.
    The 'customer_id' from the payload is used both in the URL and as the routing_id header.

    Args:
        payload (dict): Must include:
            - customer_id (str): Unique identifier of the customer.

    Returns:
        dict: Parsed JSON response from the Juspay Get Customer API, typically containing
              customer details.

    Raises:
        ValueError: If 'customer_id' is missing in the payload.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    customer_id = payload.get("customer_id")
    if not customer_id:
        raise ValueError("The payload must include 'customer_id'.")

    api_url = ENDPOINTS["customer"].format(customer_id=customer_id)
    await call(api_url, customer_id)
