import httpx
from juspay_tools.config import get_json_headers, ENDPOINTS

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
    
    routing_id = payload.get("customer_id")
    headers = get_json_headers(routing_id=routing_id)
    api_url = ENDPOINTS["session"]

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay Session API at: {api_url} with payload: {payload}")
            response = await client.post(api_url, headers=headers, json=payload)
            response.raise_for_status() 
            response_data = response.json()
            print(f"Session API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = "Unknown error"
            try:
                error_content = e.response.text
            except Exception:
                pass
            print(f"HTTP Error calling Juspay Session API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay Session API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Juspay Session API call: {e}")
            raise Exception(f"Failed to call Juspay Session API: {e}") from e