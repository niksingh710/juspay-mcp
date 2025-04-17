import httpx
from juspay_tools.config import get_form_headers, ENDPOINTS

async def create_refund_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Refund API securely using httpx with a POST request.
    
    Args:
        payload (dict): A dictionary with the following required keys:
            - order_id: Order identifier to be inserted in the URL.
            - unique_request_id: Unique refund request ID.
            - amount: Refund amount as a string.
    
    Returns:
        dict: The parsed JSON response from the Juspay Refund API.
    
    Raises:
        Exception: If the API call fails.
    """
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    
    routing_id = payload.get("customer_id", "default_routing_id")
    headers = get_form_headers(routing_id)
    headers["version"] = "2023-06-30"

    api_url = ENDPOINTS["refund"].format(order_id=order_id)
    
    # Prepare the form data for the POST request.
    # We are sending "unique_request_id" and "amount" as form-url-encoded data.
    form_data = {
        "unique_request_id": payload.get("unique_request_id"),
        "amount": payload.get("amount"),
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay Refund API at: {api_url} with form data: {form_data}")
            response = await client.post(api_url, headers=headers, data=form_data)
            response.raise_for_status()
            response_data = response.json()
            print(f"Refund API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = e.response.text if e.response is not None else "Unknown error"
            print(f"HTTP Error calling Refund API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay Refund API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Refund API call: {e}")
            raise Exception(f"Failed to call Juspay Refund API: {e}") from e
