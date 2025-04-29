from typing import Optional, Literal
from pydantic import BaseModel, Field

from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayReportDetailsPayload(WithHeaders):
    task_uid: str = Field(
        ...,
        description="Unique identifier for the report/task to retrieve details for."
    )
    user_name: str = Field(
        ...,
        description="Name of the user requesting the report."
    )

class JuspayListReportPayload(WithHeaders):
    merchantId: str = Field(
        ...,
        description="Merchant identifier for which to list reports."
    )
    task_type: Literal["report"] = Field(
        "report",
        description="Type of task to list. Must be 'report'."
    )
    std_report: Optional[bool] = Field(
        None,
        description="Optional flag to filter standard reports."
    )