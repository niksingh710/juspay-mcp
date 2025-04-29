from pydantic import BaseModel

class JuspayListSurchargeRulesPayload(BaseModel):
    """No input required. Returns a list of all configured surcharge rules, including their current status and rule definitions."""
    pass