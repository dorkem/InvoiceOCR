from domain.ocr_job import OcrJob
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from dto.ocr_job_response import OcrJobResponse

router = APIRouter(prefix="/v1/ocr", tags=["OCR"])


@router.post("/jobs", response_model=OcrJobResponse, status_code=202)
async def receive_ocr_job(
    row_id: str = Form(...),
    requirement_id: str = Form(...),
    item_name: str = Form(...),
    site_name: str = Form(...),
    invoice_image: UploadFile = File(...),
):
    # IQMS → OCR 접수용 API
    # TODO: 파일저장 ocr, 큐

    if invoice_image.content_type not in ("image/png", "image/jpeg"):
        raise HTTPException(status_code=400, detail="Only PNG/JPEG allowed")

    job = OcrJob.create(
        row_id=row_id,
        requirement_id=requirement_id,
        item_name=item_name,
        site_name=site_name,
    )

    print(
        f"[RECEIVED] job_id={job.job_id}, "
        f"row_id={row_id}, requirement_id={requirement_id}, "
        f"item={item_name}, site={site_name}, "
        f"filename={invoice_image.filename}"
    )

    return OcrJobResponse(
        job_id=job.job_id,
        status=job.status,
        received_at=job.created_at,
    )
