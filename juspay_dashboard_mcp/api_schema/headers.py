from pydantic import BaseModel, Field
from typing import Optional

class WithHeaders(BaseModel):
    # cookie: str = Field(
    #     ...,
    #     description="Authentication cookie or session token."
    # )
    tenant_id: Optional[str] = Field(
        None,
        description="Tenant identifier for multi-tenant environments."
    )
    # web_login_str field removed - now using environment variable instead
