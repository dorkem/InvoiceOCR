from pydantic import BaseModel
from datetime import datetime


class OcrJobResponse(BaseModel):
    job_id: str
    row_id: str
    requirement_id: str
    status: str
    received_at: datetime
