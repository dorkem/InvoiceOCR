import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_receive_ocr_job_success():
    data = {
        "row_id": "ROW001",
        "requirement_id": "REQ001",
        "item_name": "철근",
        "site_name": "태화강 IPARK",
    }

    fake_image = io.BytesIO(b"fake image content")
    fake_image.name = "invoice.png"

    files = {
        "invoice_image": ("invoice.png", fake_image, "image/png")
    }

    response = client.post(
        "/v1/ocr/jobs",
        data=data,
        files=files,
    )

    assert response.status_code == 202

    body = response.json()

    assert "job_id" in body
    assert body["job_id"].startswith("ocrjob_")

    assert body["status"] == "RECEIVED"
    assert "received_at" in body

    assert body["row_id"] == "ROW001"
    assert body["requirement_id"] == "REQ001"
