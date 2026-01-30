from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


class OcrJobStatus(str, Enum):
    RECEIVED = "RECEIVED"
    QUEUED = "QUEUED"


@dataclass
class OcrJob:
    job_id: str
    row_id: str
    requirement_id: str
    item_name: str
    site_name: str
    status: OcrJobStatus
    created_at: datetime

    @staticmethod
    def create(
        row_id: str,
        requirement_id: str,
        item_name: str,
        site_name: str,
    ) -> "OcrJob":
        return OcrJob(
            job_id=f"ocrjob_{uuid4().hex}",
            row_id=row_id,
            requirement_id=requirement_id,
            item_name=item_name,
            site_name=site_name,
            status=OcrJobStatus.RECEIVED,
            created_at=datetime.utcnow(),
        )
