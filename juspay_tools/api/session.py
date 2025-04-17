import httpx
from juspay_tools.config import get_json_headers, ENDPOINTS

async def session_api_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Session API securely using httpx.

    Args:
        payload: A dictionary representing the JSON body for the request.

    Returns:
        A dictionary representing the parsed JSON response from Juspay.
    """

    routing_id = payload.get("customer_id", "default_routing_id")
    headers = get_json_headers(routing_id)
    api_url = ENDPOINTS["session"]

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
