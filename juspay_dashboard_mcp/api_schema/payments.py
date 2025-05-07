# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from juspay_dashboard_mcp.api_schema.headers import WithHeaders


class JuspayListPaymentLinksV1Payload(WithHeaders):
    qFilters: Optional[Dict[str, Any]] = Field(
        None,
        description="Q API filters for payment links, e.g., order_source_object, payment_status, order_type."
    )
    filters: Dict[str, Any] = Field(
        ...,
        description="Filters for the payment links. Must include a dateCreated filter with lte and gte."
    )