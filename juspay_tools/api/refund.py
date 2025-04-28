import httpx
from juspay_tools.config import get_form_headers, ENDPOINTS

async def create_refund_juspay(payload: dict) -> dict:
    """
    Initiates a refund for a previously successful Juspay order.

    This function sends an HTTP POST request (form URL-encoded) to the Juspay Refund endpoint.
    The 'order_id' is part of the URL. 'unique_request_id' and 'amount' are sent as form data.
    If 'customer_id' is present in the payload, it's used for the routing_id header.

    Args:
        payload (dict): Must include:
            - order_id (str): Unique identifier of the order to be refunded.
            - unique_request_id (str): A unique identifier for this refund attempt.
            - amount (str): The amount to be refunded (e.g., "50.00").
        May include:
            - customer_id (str, optional): If provided, used for the x-routing-id header.

    Returns:
        dict: Parsed JSON response from the Juspay Refund API, indicating the status
              of the refund request.

    Raises:
        ValueError: If 'order_id', 'unique_request_id', or 'amount' are missing.
        Exception: If the API call fails (e.g., HTTP error, network issue).
    """
    order_id = payload.get("order_id")
    unique_request_id = payload.get("unique_request_id")
    amount = payload.get("amount")

    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    if not unique_request_id:
        raise ValueError("The payload must include 'unique_request_id'.")
    if not amount:
         raise ValueError("The payload must include 'amount'.")

    
    routing_id = payload.get("customer_id")
    headers = get_form_headers(routing_id=routing_id)
    
    api_url = ENDPOINTS["refund"].format(order_id=order_id)
    
    form_data = {
        "unique_request_id": unique_request_id,
        "amount": amount,
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