from pydantic import BaseModel, Field
from typing import Optional, Literal

class JuspayAlertDetailsPayload(BaseModel):
    task_uid: str = Field(
        ...,
        description="Unique alert ID for which details are to be fetched."
    )
    user_name: str = Field(
        ...,
        description="User name associated with the alert."
    )

class JuspayListAlertsPayload(BaseModel):
    merchantId: str = Field(
        ...,
        description="Merchant ID for which alerts are to be listed."
    )
    task_type: Literal["alert"] = Field(
        ...,
        description="Type of monitoring task. Should be 'alert'."
    )