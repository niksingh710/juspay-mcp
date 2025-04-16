import os
import base64
import json
import httpx

JUSPAY_API_KEY = os.getenv("JUSPAY_API_KEY")
JUSPAY_MERCHANT_ID = os.getenv("JUSPAY_MERCHANT_ID")

async def create_refund_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Refund API securely using httpx with a POST request.
    
    The API endpoint is:
        https://api.juspay.in/orders/{order_id}/refunds
    
    The call uses form-url-encoded data containing:
        - unique_request_id (e.g., "xyz123")
        - amount (e.g., "100.00")
    
    Headers include:
        - Basic Authorization derived from JUSPAY_API_KEY
        - version: 2023-06-30
        - x-routing-id: customer_1122
        - x-merchantid from environment variable
    
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
    if not JUSPAY_API_KEY or not JUSPAY_MERCHANT_ID:
        raise ValueError("JUSPAY_API_KEY and JUSPAY_MERCHANT_ID environment variables must be set.")
    
    order_id = payload.get("order_id")
    if not order_id:
        raise ValueError("The payload must include 'order_id'.")
    
    # Build the API URL using the order id.
    api_url = f"https://api.juspay.in/orders/{order_id}/refunds"

    # Prepare the Basic Authentication header.
    auth_string = f"{JUSPAY_API_KEY}:"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "version": "2023-06-30",
        "x-routing-id": "customer_1122",  # As per the cURL sample; adjust as needed.
        "x-merchantid": JUSPAY_MERCHANT_ID,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    
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
