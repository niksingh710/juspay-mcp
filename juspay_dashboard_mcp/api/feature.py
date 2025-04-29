import logging

from juspay_dashboard_mcp.api.utils import post, get_juspay_host_from_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

async def fetch_feature_details_juspay(payload: dict) -> dict:
    """
    Provides comprehensive information for a specific feature ID, including overview, description, FAQs, usage by other merchants, supported PGs/PMTs/platforms, and related features.

    Args:
        payload (dict): Must contain 'merchant_id' and 'feature_id'. 'client_id' is optional.

    Returns:
        dict: The parsed JSON response from the Juspay Fetch Feature Details API.

    Raises:
        Exception: If the API call fails.
    """
    host = await get_juspay_host_from_api(token=payload.get("web_login_str"))
    api_url = f"{host}stein/feature-description/fetch"
    return await post(api_url, payload)

