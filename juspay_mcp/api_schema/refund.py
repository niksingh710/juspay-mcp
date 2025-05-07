# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

from pydantic import Field
from juspay_mcp.api_schema.routing import WithRoutingId

class JuspayTxnRefundPayload(WithRoutingId):
    txn_id: str = Field(..., description="Transaction ID to be refunded (e.g., 'merchant_id-order_id-1').")
    unique_request_id: str = Field(..., description="Unique identifier for this refund request.")
    amount: str = Field(..., description="Refund amount as a string (e.g., '100.00').")


class JuspayRefundPayload(WithRoutingId):
    order_id: str = Field(..., description="Unique identifier of the order to refund.")
    unique_request_id: str = Field(..., description="Unique refund request identifier (e.g., 'xyz123').")
    amount: str = Field(..., description="Refund amount as a string (e.g., '100.00').")
