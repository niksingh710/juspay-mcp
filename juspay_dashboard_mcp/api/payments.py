import logging
from juspay_dashboard_mcp.api.utils import post, get_juspay_host_from_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def list_payment_links_v1_juspay(payload: dict) -> dict:
    """
    Calls the Juspay Portal API to retrieve a list of payment links within a specified time range.

    Args:
        payload (dict): A dictionary containing:
            - dateFrom: Start date/time in ISO format (e.g., '2025-04-15T18:30:00Z')
            - dateTo: End date/time in ISO format (e.g., '2025-04-16T15:08:10Z')
            - offset: Pagination offset (optional, default 0)

    Returns:
        dict: The parsed JSON response from the List Payment Links API.

    Raises:
        Exception: If the API call fails.
    """
    host = await get_juspay_host_from_api(token=payload.get("web_login_str"))
    api_url = f"{host}api/ec/v1/paymentLinks/list"
    request_data = {
        "qFilters": {
            "field": "order_source_object",
            "condition": "Equals",
            "val": "PAYMENT_LINK"
        },
        "filters": {
            "dateCreated": {
                "lte": payload["dateTo"],
                "gte": payload["dateFrom"],
                "opt": "custom_range"
            }
        }
    }
    if "offset" in payload:
        request_data["offset"] = payload["offset"]
    return await post(api_url, request_data)