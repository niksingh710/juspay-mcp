from pydantic import BaseModel, Field

class WithHeaders(BaseModel):
    cookie: str = Field(
        ...,
        description="Authentication cookie or session token."
    )
    tenant_id: str = Field(
        ...,
        description="Tenant identifier for multi-tenant environments."
    )
    # web_login_str field removed - now using environment variable instead
