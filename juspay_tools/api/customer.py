import httpx
from juspay_tools.config import get_form_headers, ENDPOINTS

async def get_customer_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Get Customer API securely using httpx with a GET request.
    
    Args:
        payload (dict): Must include:
            - customer_id (str): Unique identifier of the customer.
    
    Returns:
        dict: Parsed JSON response from the Juspay Get Customer API.
    
    Raises:
        Exception: If the API call fails.
    """
    customer_id = payload.get("customer_id")
    if not customer_id:
        raise ValueError("The payload must include 'customer_id'.")
    
    routing_id = customer_id
    headers = get_form_headers(routing_id)
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
