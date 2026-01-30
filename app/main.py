from fastapi import FastAPI
from app.api.v1.ocr.ocr_job_router import router as ocr_job_router

app = FastAPI()

app.include_router(ocr_job_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
