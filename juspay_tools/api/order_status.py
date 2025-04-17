import httpx
from juspay_tools.config import get_json_headers, ENDPOINTS

async def order_status_api_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Order Status API securely using httpx with a GET request.
    
    This function sends an HTTP GET request to the Juspay Order Status endpoint,
    appending the 'order_id' from the payload to the URL.
    
    Args:
        payload (dict): A dictionary with the required key "order_id".
    
    Returns:
        dict: The parsed JSON response from the Juspay Order Status API.
    
    Raises:
        Exception: If the API call fails.
    """
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    
    routing_id = payload.get("customer_id", "default_routing_id")
    headers = get_json_headers(routing_id)

    api_url = ENDPOINTS["order_status"].format(order_id=order_id)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay Order Status API at: {api_url}")
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            print(f"Order Status API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = e.response.text if e.response is not None else "Unknown error"
            print(f"HTTP Error calling Juspay Order Status API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay Order Status API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Juspay Order Status API call: {e}")
            raise Exception(f"Failed to call Juspay Order Status API: {e}") from e
