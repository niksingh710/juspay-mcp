import httpx
from juspay_tools.config import get_form_headers

async def call(api_url: str, customer_id: str | None = None) -> dict:
    headers = get_form_headers(routing_id=customer_id) 

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay API at: {api_url}")
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            print(f"Get API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = e.response.text if e.response is not None else "Unknown error"
            print(f"HTTP Error calling Juspay API: {e.status_code} - {error_content}")
            raise Exception(f"Juspay API Error ({e.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Juspay API call: {e}")
            raise Exception(f"Failed to call Juspay API: {e}") from e

async def post(api_url: str, payload: dict, routing_id: str | None = None) -> dict:
    effective_routing_id = routing_id or payload.get("customer_id")
    headers = get_form_headers(routing_id=effective_routing_id) 

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print(f"Calling Juspay API at: {api_url}")
            response = await client.post(api_url, headers=headers, data=payload)
            response.raise_for_status()
            response_data = response.json()
            print(f"API Response Data: {response_data}")
            return response_data
        except httpx.HTTPStatusError as e:
            error_content = e.response.text if e.response is not None else "Unknown error"
            print(f"HTTP Error calling Juspay API: {e.response.status_code} - {error_content}")
            raise Exception(f"Juspay API Error ({e.response.status_code}): {error_content}") from e
        except Exception as e:
            print(f"Error during Juspay API call: {e}")
            raise Exception(f"Failed to call Juspay API: {e}") from e