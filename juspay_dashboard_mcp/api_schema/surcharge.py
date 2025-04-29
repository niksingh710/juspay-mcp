from pydantic import BaseModel
from juspay_dashboard_mcp.api_schema.headers import WithHeaders


class JuspayListSurchargeRulesPayload(WithHeaders):
    """No input required. Returns a list of all configured surcharge rules, including their current status and rule definitions."""
    pass