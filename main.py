from api.v1.ocr import ocr_job_router
from fastapi import FastAPI

app = FastAPI(title="OCR API (POC)")

app.include_router(ocr_job_router)