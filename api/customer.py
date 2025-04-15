import os
import base64
import httpx
import json
import dotenv

dotenv.load_dotenv()

JUSPAY_API_KEY = os.getenv("JUSPAY_API_KEY")
JUSPAY_MERCHANT_ID = os.getenv("JUSPAY_MERCHANT_ID")

async def get_customer_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Get Customer API securely using httpx with a GET request.
    
    The API endpoint is constructed by appending the provided customer_id to:
        https://api.juspay.in/customers/{customer_id}
    
    The call uses basic authentication (via API key) and required headers.
    
    Args:
        payload (dict): Must include:
            - customer_id (str): Unique identifier of the customer.
    
    Returns:
        dict: Parsed JSON response from the Juspay Get Customer API.
    
    Raises:
        Exception: If the API call fails.
    """
    if not JUSPAY_API_KEY or not JUSPAY_MERCHANT_ID:
        raise ValueError("JUSPAY_API_KEY and JUSPAY_MERCHANT_ID environment variables must be set.")
    
    customer_id = payload.get("customer_id")
    if not customer_id:
        raise ValueError("The payload must include 'customer_id'.")
    
    api_url = f"https://api.juspay.in/customers/{customer_id}"
    
    # Prepare the Basic Authentication header.
    auth_string = f"{JUSPAY_API_KEY}:"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "x-merchantid": JUSPAY_MERCHANT_ID,
        "x-routing-id": "customer_1122",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    
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
