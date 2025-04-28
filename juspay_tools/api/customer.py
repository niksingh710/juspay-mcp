import httpx
from juspay_tools.config import get_form_headers, ENDPOINTS 

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

    
    headers = get_form_headers(routing_id=customer_id) 
    api_url = ENDPOINTS["customer"].format(customer_id=customer_id)

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay Get Customer API at: {api_url}")
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            print(f"Get Customer API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = e.response.text if e.response is not None else "Unknown error"
            print(f"HTTP Error calling Get Customer API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay Get Customer API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Get Customer API call: {e}")
            raise Exception(f"Failed to call Juspay Get Customer API: {e}") from e