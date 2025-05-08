# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

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
