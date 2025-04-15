import base64 
import os
import httpx

JUSPAY_API_KEY = os.getenv("JUSPAY_API_KEY")
JUSPAY_MERCHANT_ID = os.getenv("JUSPAY_MERCHANT_ID")

async def session_api_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Session API securely using httpx.

    Args:
        payload: A dictionary representing the JSON body for the request.

    Returns:
        A dictionary representing the parsed JSON response from Juspay.
    """

    if not JUSPAY_API_KEY or not JUSPAY_MERCHANT_ID:
        raise ValueError("JUSPAY_API_KEY and JUSPAY_MERCHANT_ID environment variables must be set.")

    api_url = "https://sandbox.juspay.in/session" 

    auth_string = f"{JUSPAY_API_KEY}:"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "x-merchantid": JUSPAY_MERCHANT_ID,
        "x-routing-id": payload.get("customer_id", "default_routing_id"), 
        "Content-Type": "application/json",
        "Accept": "application/json", 
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(api_url, headers=headers, json=payload)
            response.raise_for_status() 
            response_data = response.json()
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = "Unknown error"
            try:
                error_content = e.response.text 
            except Exception:
                pass 
            print(f"HTTP Error calling Juspay API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Juspay API call: {e}")
            raise Exception(f"Failed to call Juspay Session API: {e}") from e
