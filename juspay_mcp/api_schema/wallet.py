# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

from pydantic import Field

from juspay_mcp.api_schema.routing import WithRoutingId

class ListWalletsPayload(WithRoutingId):
    customer_id: str = Field(
        ...,
        description="Unique identifier for the customer whose wallets are to be listed."
    )
